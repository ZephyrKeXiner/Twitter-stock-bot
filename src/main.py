from services.twitter_service import TwitterService
from services.crypto_service import CryptoService
from services.news_service import NewsService
from datetime import datetime

def build_market_tweet(btc_price, btc_change, eth_price, eth_change):
    now = datetime.now().strftime("%Y-%m-%d")
    tweet = f"""📊 {now} 市场动态

🟠 BTC: ${btc_price:,.0f} ({btc_change:+.2f}%)
🔵 ETH: ${eth_price:,.0f} ({eth_change:+.2f}%)

#美股 #加密货币 #BTC #ETH #投资"""
    return tweet

def main():
    try:
        # 获取数据
        crypto_service = CryptoService()
        btc_price, btc_change, eth_price, eth_change = crypto_service.get_crypto_prices()

        news_service = NewsService()
        news = news_service.get_stock_news()

        # 构造推文
        market_tweet = build_market_tweet(btc_price, btc_change, eth_price, eth_change)

        # 发推
        twitter_service = TwitterService()
        if len(market_tweet + "\n\n" + news) <= 280:
            twitter_service.post_tweet(market_tweet + "\n\n" + news)
        else:
            response = twitter_service.post_tweet(market_tweet)
            tweet_id = response.data["id"]
            twitter_service.post_tweet(news, in_reply_to_tweet_id=tweet_id)

        print("✅ 推文成功发送")

    except Exception as e:
        print("❌ 出错了:", e)

if __name__ == "__main__":
    main()