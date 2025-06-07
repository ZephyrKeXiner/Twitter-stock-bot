from datetime import datetime, timedelta
import investpy

class EventCalendar:
    def get_us_events_today(self) -> str:
        return self._get_events_by_country(['united states', 'china', 'hongkong'])

    def _get_events_by_country(self, countries) -> str:
        today = datetime.now()
        tomorrow = today + timedelta(days=1)

        from_date = today.strftime('%d/%m/%Y')
        to_date = tomorrow.strftime('%d/%m/%Y')

        try:
            df = investpy.economic_calendar(
                countries=countries,
                from_date=from_date,
                to_date=to_date
            )
            if df.empty:
                return "📭 今天暂无重要经济数据公布"

            events = []
            for _, row in df.iterrows():
                importance = row['importance'].lower()
                if importance in ['medium', 'high']:
                    currency = row.get('currency', '').upper()
                    date = row['date']
                    time = row['time']
                    event = row['event']

                    if currency == 'USD':
                        flag = "🇺🇸"
                    elif currency == 'CNY':
                        flag = "🇨🇳"
                    elif currency == 'HKD':
                        flag = "🇭🇰"
                    else:
                        continue  # 跳过非美中货币事件

                    events.append(f"{flag} {date} {time} - {event} ({importance.capitalize()})")

            if not events:
                return "📭 今天暂无中高重要度的美中经济事件"

            return "\n".join(events)
        except Exception as e:
            return f"❗ 获取经济日历失败: {e}"
        
if __name__ == '__main__':
    calendar = EventCalendar()
    events_text = calendar.get_us_events_today()
    print(events_text)