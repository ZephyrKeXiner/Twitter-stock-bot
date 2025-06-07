from services.twitter_service import TwitterService
from services.crypto_service import CryptoService
from services.news_service import NewsService
from services.event_calendar import EventCalendar
from datetime import datetime
import os

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

        # 构造推文
        market_tweet = build_market_tweet(crypto_data)

        # 检查调试模式
        debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"

        tweet_content = market_tweet + "\n\n" + events_text + "\n\n" + news

        if debug_mode:
            print("🛠 调试模式启用")
            print("构造的推文内容:")
            print(tweet_content)
        else:
            # 发推
            twitter_service = TwitterService()
            if len(tweet_content) <= 280:
                twitter_service.post_tweet(tweet_content)
            else:
                response = twitter_service.post_tweet(market_tweet)
                tweet_id = response.data["id"]
                # 事件和新闻分开发送
                twitter_service.post_tweet(events_text, in_reply_to_tweet_id=tweet_id)
                twitter_service.post_tweet(news, in_reply_to_tweet_id=tweet_id)

            print("✅ 推文成功发送")

    except Exception as e:
        print("❌ 出错了:", e)

if __name__ == "__main__":
    main()