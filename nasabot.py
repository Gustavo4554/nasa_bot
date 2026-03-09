import requests
import os

def enviar_nasa():
    # Puxa os segredos
    key = os.getenv('TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk')
    token = os.getenv('8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0')
    chat = os.getenv('8684474222')

    print(f"Tentando com o Chat ID: {chat}") # Isso vai aparecer no log do GitHub

    # Busca na NASA
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    res = requests.get(url).json()
    titulo = res.get('title', 'Notícia Espacial')
    link_img = res.get('url', '')
    
    # Envia pro Telegram
    url_tg = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat, "text": f"🚀 {titulo}\n\n{link_img}"}
    
    # PEGA A RESPOSTA DO TELEGRAM
    resposta = requests.post(url_tg, data=payload)
    
    print(f"Status do Telegram: {resposta.status_code}")
    print(f"Mensagem do Telegram: {resposta.text}")

if __name__ == "__main__":
    enviar_nasa()
