import requests

# COLOQUE SEUS CÓDIGOS DIRETAMENTE ENTRE AS ASPAS
NASA_KEY = "TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk"
TG_TOKEN = "8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0"
CHAT_ID = "8684474222"

def pegar_dados_nasa():
    # Agora a chave vai direto na URL
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na NASA: {response.status_code}")
        return None

def enviar_telegram(titulo, texto, imagem):
    resumo = (texto[:500] + '...') if len(texto) > 500 else texto
    mensagem = f"🔭 *{titulo}*\n\n{resumo}\n\n📸 {imagem}"
    
    url_tg = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": mensagem, 
        "parse_mode": "Markdown"
    }
    
    envio = requests.post(url_tg, data=payload)
    if envio.status_code == 200:
        print("✅ Mensagem enviada com sucesso!")
    else:
        print(f"❌ Erro no Telegram: {envio.text}")

if __name__ == "__main__":
    dados = pegar_dados_nasa()
    if dados:
        enviar_telegram(
            dados.get('title', 'Sem título'), 
            dados.get('explanation', 'Sem descrição'), 
            dados.get('url', '')
        )
    else:
        print("Não foi possível carregar os dados da NASA.")
