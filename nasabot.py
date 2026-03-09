import requests
import time
from deep_translator import GoogleTranslator

# --- SEUS DADOS ---
NASA_KEY = "TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk"
TG_TOKEN = "8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0"
CHAT_ID = "8684474222"

def traduzir(texto):
    try:
        # Traduz do inglês para o português
        return GoogleTranslator(source='en', target='pt').translate(texto)
    except:
        return texto

def pegar_10_noticias():
    # 'count=10' traz 10 notícias aleatórias com explicações
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}&count=10"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na NASA: {response.status_code}")
        return None

def enviar_telegram(titulo, texto, imagem):
    print(f"Traduzindo: {titulo}")
    titulo_pt = traduzir(titulo)
    texto_pt = traduzir(texto)
    
    # Limita o texto para não ultrapassar o limite do Telegram
    resumo = (texto_pt[:900] + '...') if len(texto_pt) > 900 else texto_pt
    
    # Monta a mensagem com Título, Explicação e Link da Imagem
    mensagem = f"🔭 *{titulo_pt}*\n\n📝 {resumo}\n\n📸 {imagem}"
    
    url_tg = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": mensagem, 
        "parse_mode": "Markdown"
    }
    
    requests.post(url_tg, data=payload)

if __name__ == "__main__":
    lista = pegar_10_noticias()
    if lista:
        for item in lista:
            enviar_telegram(
                item.get('title', 'Sem título'), 
                item.get('explanation', 'Sem descrição'), 
                item.get('url', '')
            )
            # Pausa de 3 segundos para o Telegram não bloquear por spam
            time.sleep(3) 
        print("✅ 10 notícias enviadas com sucesso!")
    else:
        print("Não foi possível carregar os dados.")
