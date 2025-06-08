from services.twitter_service import TwitterService
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

def safe_post(twitter_service, text, reply_id=None):
    if len(text) > 260:
        raise Exception(f"❗ 推文长度超限：{len(text)} 字，最大允许 260 字")
    return twitter_service.post_tweet(text, in_reply_to_tweet_id=reply_id)

def post_long_tweet(ts, text):
    # 将文本拆分为多个不超 260 字的部分，依次发送并建立回复链
    parts = []
    while len(text) > 260:
        chunk = text[:260]
        sep = max(chunk.rfind('\n'), chunk.rfind(' '))
        if sep > 0:
            parts.append(chunk[:sep])
            text = text[sep:].lstrip()
        else:
            parts.append(chunk)
            text = text[260:]
    parts.append(text)

    reply_id = None
    resp = None
    for part in parts:
        resp = ts.post_tweet(part, in_reply_to_tweet_id=reply_id)
        reply_id = resp.data["id"]
    return resp

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

        # 构造推文
        market_message = build_market_tweet(crypto_data)
        tweet_content = market_message + "\n\n" + events_text + "\n\n" + news + "\n\n" + summary
        if send_way == 'twitter':
          # 检查调试模式
          debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
          if debug_mode:
              print("🛠 调试模式启用\n", tweet_content)
          else:
              twitter_service = TwitterService()
              print(twitter_service.verify_credentials())
              # 使用 post_long_tweet 自动拆分并发送
              post_long_tweet(twitter_service, tweet_content)
              print("✅ 推文成功发送")
        elif send_way == 'telegram':
          telegram_bot = TelegramBot()
          telegram_bot.send_telegram_message(tweet_content)
    except Exception as e:
        print("❌ 出错了:", e)

if __name__ == "__main__":
    main()