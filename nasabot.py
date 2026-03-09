import requests
import os

# Substitua ou use variáveis de ambiente (melhor para segurança)
NASA_KEY = "TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk"
TG_TOKEN = "8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0"
CHAT_ID = "8684474222"

def pegar_dados_nasa():
    url = f"https://api.nasa.gov/planetary/apod?api_key={TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def enviar_telegram(titulo, texto, imagem):
    # Corta o texto se for muito longo para o Telegram
    resumo = (texto[:400] + '...') if len(texto) > 400 else texto
    mensagem = f"🔭 *{titulo}*\n\n{resumo}\n\n📸 {imagem}"
    
    url = f"https://api.telegram.org/bot{8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

if __name__ == "__main__":
    dados = pegar_dados_nasa()
    if dados:
        enviar_telegram(dados.get('title'), dados.get('explanation'), dados.get('url'))