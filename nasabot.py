import requests
import os

# O código abaixo busca as chaves que você salvou no GitHub Settings
# Assim, o seu código fica protegido e funciona no servidor do GitHub
NASA_KEY = os.getenv('TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk')
TG_TOKEN = os.getenv('8294119351:AAFxdGkUOb3FRvVOxH31uCizVan8jCIlSD0')
CHAT_ID = os.getenv('8684474222')

def pegar_dados_nasa():
    # Aqui usamos a variável NASA_KEY que definimos acima
    url = f"https://api.nasa.gov/planetary/apod?api_key={TPietevSID71LaSZcqKEBwBbQWoyJ2hOvFkjr4sk}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro na NASA: Status {response.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")
    return None

def enviar_telegram(titulo, texto, imagem):
    # Corta o texto se for muito longo para o Telegram não dar erro
    resumo = (texto[:400] + '...') if len(texto) > 400 else texto
    mensagem = f"🔭 *{titulo}*\n\n{resumo}\n\n📸 {imagem}"
    
    # Aqui usamos o TG_TOKEN que definimos no topo do código
    url_tg = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {
        "chat_id": 8684474222, 
        "text": mensagem, 
        "parse_mode": "Markdown"
    }
    
    try:
        post = requests.post(url_tg, data=payload)
        print(f"Resposta do Telegram: {post.status_code}")
    except Exception as e:
        print(f"Erro ao enviar para o Telegram: {e}")

if __name__ == "__main__":
    dados = pegar_dados_nasa()
    if dados:
        enviar_telegram(
            dados.get('title', 'Sem título'), 
            dados.get('explanation', 'Sem descrição'), 
            dados.get('url', '')
        )
    else:
        print("Não foi possível obter dados da NASA hoje.")
