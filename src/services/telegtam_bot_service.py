import requests
from utils.config import Config

class TelegramBot():
  def __init__(self):
    config = Config()
    self.CHAT_ID = config.CHAT_ID
    self.BOT_TOKEN =config.BOT_TOKEN

  def send_telegram_message(self, text: str):
    url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
    data = {
      "chat_id": self.CHAT_ID,
      "text": text
    }

    r = requests.post(url, data=data)
    if r.status_code != 200:
      print("❌ 消息发送失败:", r.text)
    else:
      print("✅ 消息已发送")
