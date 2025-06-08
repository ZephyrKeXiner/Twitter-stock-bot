from services.telegtam_bot_service import TelegramBot
from services.news_service import NewsService
from services.event_calendar import EventCalendar
from services.ai_service import SummaryGenerator

news_service = NewsService()
news = news_service.get_stock_news()
calendar = EventCalendar()
events_text = calendar.get_us_events_today()
ai = SummaryGenerator()
summary = ai.generate_summary(news, events_text)

tweet_content = "\n\n" + events_text + "\n\n" + news + "\n\n" + summary

telegram_bot = TelegramBot()
telegram_bot.send_telegram_message(tweet_content)
