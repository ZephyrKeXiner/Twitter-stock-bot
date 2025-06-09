# file: bot_listener.py
import os
import json
import requests
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_FILE = "users.json"

app = Flask(__name__)

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(list(users), f)

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    users = load_users()
    if chat_id not in users:
        users.add(chat_id)
        save_users(users)
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": chat_id, "text": "✅ 你已成功订阅每日简报"}
        )
    return "ok"
