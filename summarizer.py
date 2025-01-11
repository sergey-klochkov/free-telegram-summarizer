import google.generativeai as genai
from typing import Optional

def init_gemini(api_key: Optional[str] = None) -> None:
    if not api_key:
        raise ValueError('API key must be provided or set as GOOGLE_API_KEY environment variable')

    genai.configure(api_key=api_key)


def summarize_text(text: str, api_key: Optional[str] = None) -> str:
    try:
        if not text.strip():
            raise ValueError('Input text cannot be empty or just whitespace.')

        init_gemini(api_key)
        prompt = f'Please summarize the following conversation in Russian language. Focus on the main points and key information:\n\n{text}'

        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        response = model.generate_content(prompt)

        if response and hasattr(response, 'text'):
            return response.text
        else:
            raise Exception('Empty or invalid response received from the model.')
    except ValueError as e:
        raise ValueError(f'Input validation failed: {str(e)}')
    except Exception as e:
        raise Exception(f'Summarization failed: {str(e)}')
