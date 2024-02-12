# Standard library imports.
import os
import time
import requests

# Third party imports.
import openai
from openai import OpenAI


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

TOKEN = os.environ.get('TELEGRAM_TOKEN')


def get_updates(offset):
    """https://core.telegram.org/bots/api"""
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()['result']

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt, model):
    """https://platform.openai.com/docs/guides/error-codes/api-errors"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Eres un asistente de atención a clientes y estudiantes de la plataforma de educación online en tecnología, inglés y liderazgo llamada Platzi"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            temperature=1,
            stop=" END",
        )
        return response.choices[0].message.content.strip()
    except openai.APIError as e:
        # Manejar error de API aquí, p. reintentar o iniciar sesión
        print(f"La API de OpenAI devolvió un error de API: {e}")
        pass  # Aprobar
    except openai.APIConnectionError as e:
        # Manejar error de conexión aquí
        print(f"Error al conectarse a la API de OpenAI: {e}")
        pass
    except openai.RateLimitError as e:
        # Manejar error de límite de tasa (recomendamos usar retroceso exponencial)
        print(f"La solicitud de API de OpenAI excedió el límite de frecuencia: {e}")
        pass

    return "Ocurrió un Error :("


def main():
    print("Starting bot ...")
    offset = 0
    while True:
        updates = get_updates(offset)
        if updates:
            for update in updates:
                offset = update['update_id'] + 1
                chat_id = update['message']['chat']['id']
                user_message = update['message']['text']
                print(f"Received message: {user_message}")

                GPT = get_openai_response(user_message,
                                          model=os.environ.get('OPENAI_PLATZI_MODEL'))
                send_message(chat_id, GPT)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
