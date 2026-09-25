import os
from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "@Ofertas40pe")

@app.route("/")
def home():
    return "BOT OFERTAS40 ACTIVO 24/7"

def enviar_mensaje(texto):
    if not BOT_TOKEN:
        return
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
    except:
        pass

def loop_bot():
    time.sleep(10)
    enviar_mensaje("✅ Bot OFERTAS40 conectado y activo 24/7 en Render")
    while True:
        time.sleep(3600)

threading.Thread(target=loop_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
