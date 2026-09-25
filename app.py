import os, threading, time, requests
from flask import Flask
app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8570656352:AAGFlVfsjo3y4dHG4_vY3FZdiyM70m_CpfQ")
CHAT_ID = os.environ.get("CHAT_ID", "")
@app.route("/")
def home():
    return "BOT OFERTAS40 ACTIVO"
def send(msg):
    if not CHAT_ID: return
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id":CHAT_ID,"text":msg}, timeout=10)
    except: pass
def loop():
    time.sleep(5)
    send("Bot OFERTAS40 activado!")
    while True:
        time.sleep(3600)
threading.Thread(target=loop, daemon=True).start()
