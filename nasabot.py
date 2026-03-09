import requests
import os

# O Python vai buscar o CONTEÚDO que está guardado no GitHub
NASA_KEY = os.getenv('NASA_KEY')
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def pegar_dados_nasa():
    # Agora o NASA_KEY vai valer o seu código secreto
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na NASA: {response.status_code}")
        return None
# ... resto do código igual ...

def enviar_telegram(titulo, texto, imagem):
    # Corta o texto se for muito longo (limite do Telegram)
    resumo = (texto[:500] + '...') if len(texto) > 500 else texto
    
    # Monta a mensagem bonita
    mensagem = f"🔭 *{titulo}*\n\n{resumo}\n\n📸 {imagem}"
    
    # Envia para o seu Bot
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
        # Puxa os campos certos do dicionário da NASA
        enviar_telegram(
            dados.get('title', 'Sem título'), 
            dados.get('explanation', 'Sem descrição'), 
            dados.get('url', '')
        )
    else:
        print("Não foi possível carregar os dados da NASA.")


