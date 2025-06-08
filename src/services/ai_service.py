from google import genai
from google.genai import types
from utils.config import Config

class SummaryGenerator:
    def __init__(self):
        self.client = genai.Client(api_key=Config().LLM_API_TOKEN)

    def generate_summary(self, news_text: str, event_text: str) -> str:
        prompt = (
            "请根据以下内容生成一段中文摘要：\n\n"
            f"【今日新闻】\n{news_text}\n\n"
            f"【经济事件】\n{event_text}\n\n"
            "要求：\n- 使用中文\n- 用客观的语言总结要点\n- 给出未来几天值得关注的地方\n "
            "请分点展开进行叙述, 帮助投资者尽可能弄清影响\n"
            "返回易于给读者读的纯文本格式，要求分点清晰，不要所有文字堆在一起，不要包含 markdown 语法\n"
        )

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash-preview-05-20", 
                config=types.GenerateContentConfig(
                    system_instruction="你是一个财经内容助手"),
                contents=prompt
            )
            return response.text
        except Exception as e:
            print("❗ GEMINI 生成摘要失败:", e)
            return "❗ 生成摘要失败"