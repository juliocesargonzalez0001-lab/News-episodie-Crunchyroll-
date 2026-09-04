import os
import feedparser
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
RSS_URL = "https://www.crunchyroll.com/rss"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def verificar_estrenos():
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        return
    
    ultima_entrada = feed.entries[0]
    titulo = ultima_entrada.title
    enlace = ultima_entrada.link
    
    mensaje = f"*{titulo}*\n\n{enlace}"
    enviar_telegram(mensaje)

if __name__ == "__main__":
    verificar_estrenos()
