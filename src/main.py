from services.crypto_service import CryptoService
from services.news_service import NewsService
from services.event_calendar import EventCalendar
from services.telegtam_bot_service import TelegramBot
from services.ai_service import SummaryGenerator
from datetime import datetime
import os

send_way = 'telegram'

def build_market_tweet(crypto_data):
    now = datetime.now().strftime("%Y-%m-%d")
    tweet = f"📊 {now} 市场动态\n\n"
    for name, data in crypto_data.items():
        price, change = data
        tweet += f"🔸 {name.upper()}: ${price:,.0f} ({change:+.2f}%)\n"
    tweet += "\n#美股 #加密货币 #投资"
    return tweet

def main():
    try:
        # 获取数据
        crypto_service = CryptoService()
        crypto_data = crypto_service.get_crypto_prices()

        news_service = NewsService()
        news = news_service.get_stock_news()
        calendar = EventCalendar()
        events_text = calendar.get_us_events_today()
        ai = SummaryGenerator()
        summary = ai.generate_summary(news, events_text)

        # 构造消息
        market_message = build_market_tweet(crypto_data)
        message_content = market_message + "\n\n" + events_text + "\n\n" + news + "\n\n" + summary

        # 使用 Telegram 发送消息
        telegram_bot = TelegramBot()
        telegram_bot.send_telegram_message(message_content)

    except Exception as e:
        print("❌ 出错了:", e)

if __name__ == "__main__":
    main()