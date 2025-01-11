from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from collections import deque
from summarizer import summarize_text, init_gemini
import os
from dotenv import load_dotenv

load_dotenv()
MAX_MESSAGES = 500
message_queue = deque(maxlen=MAX_MESSAGES)
# Replace with TG bot's token
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# set gemini token
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I\'m your summarize Bot. Usage: /summarize <number_of_messages>')


async def summarize(update: Update, context: CallbackContext):
    if len(context.args) == 1 and context.args[0].isdigit():
        num_messages = int(context.args[0])

        if num_messages <= 0:
            await update.message.reply_text('Please provide a positive number.')
            return

        available_messages = len(message_queue)
        messages_to_summarize = list(message_queue)[-min(num_messages, available_messages):]

        if messages_to_summarize:
            input_text = '\n'.join(messages_to_summarize)
            try:
                full_summary = summarize_text(input_text)
                await update.message.reply_text(f'\nSummary: {full_summary}')

            except Exception as e:
                print(f'Error: {e}')
        else:
            await update.message.reply_text('No messages to summarize.')
    else:
        await update.message.reply_text('Usage: /summarize <number_of_messages>')

async def store(update: Update, context: CallbackContext):
    text = update.message.text
    full_name = update.message.from_user.full_name
    message_queue.append(f'{full_name}: {text}')

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    init_gemini(GEMINI_API_KEY)

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', start))
    application.add_handler(CommandHandler('usage', start))
    application.add_handler(CommandHandler('summarize', summarize))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, store))
    application.run_polling()

if __name__ == '__main__':
    main()
