import requests
from utils.config import Config

class StocksService:
    def get_stock_prices(self):
        url = f"https://finnhub.io/api/v1/news?category=general&token={Config().FINNHUB_API_KEY}"
        try:
            r = requests.get(url).json()
            news_list = r[:3]  # 取前两条新闻
            news_texts = []
            for news in news_list:
                headline = news["headline"]
                link = news["url"]
                news_texts.append(f"📰 {headline}\n🔗 {link}")
            return "\n\n".join(news_texts)
        except Exception:
            return "❗ 获取新闻失败"