# About
Telegram Bot to summarize your chats without need to download any model.
This Bot uses Gemini API, which provides free tier.

# Installation and Usage
1. https://github.com/sergey-klochkov/free-telegram-summarizer-bot.git
2. Ensure you have python version >3.9
3. Install dependencies
```
pip install -q -U google-generativeai
pip install python-telegram-bot
pip install python-dotenv
```
4. Create a .env file in the root directory and add the following environment variables:
```
TELEGRAM_BOT_TOKEN=<your-tg-bot-token>
GEMINI_API_KEY=<your-gemini-api-key>
```
5. Run bot
```
python main.py
```

# Tokens
TELEGRAM_BOT_TOKEN can be obtained from tg - @BotFather

GEMINI_API_KEY can be obtained from google ai studio https://aistudio.google.com/apikey
