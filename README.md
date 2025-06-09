# 📊 Daily Market Bot / 每日市场机器人

**Daily Market Bot** is an automated tool for retrieving cryptocurrency prices, financial news, and economic events, and sending daily market briefings via Telegram.  
**每日市场机器人** 是一个自动化工具，用于获取加密货币价格、财经新闻和经济事件，并通过 Telegram 发送每日市场简报。

---

## ✨ Features / 功能

- **Real-time Cryptocurrency Prices**: Supports Bitcoin, Ethereum, and other major cryptocurrencies.  
  **实时加密货币价格**：支持 Bitcoin、Ethereum 等主流加密货币。
- **Financial News**: Fetch the latest financial news to help users understand market trends.  
  **财经新闻**：获取最新的财经新闻，帮助用户了解市场动态。
- **Economic Events**: Track important economic events for investment insights.  
  **经济事件**：追踪重要的经济事件，提供投资参考。
- **AI Summary Generation**: Automatically generate concise market summaries using AI.  
  **AI摘要生成**：通过 AI 自动生成简洁的市场摘要。
- **Telegram Messaging**: Automatically send daily market briefings to subscribed users.  
  **Telegram消息推送**：每日自动发送市场简报到订阅用户。

---

## 📂 Project Structure / 项目结构

```
daily_market_bot
├── src
│   ├── main.py               # Entry point of the application / 主程序入口
│   ├── services              # Service modules / 服务模块
│   │   ├── crypto_service.py  # Cryptocurrency data service / 加密货币数据服务
│   │   ├── news_service.py    # Financial news service / 财经新闻服务
│   │   ├── event_calendar.py  # Economic events service / 经济事件服务
│   │   ├── telegtam_bot_service.py # Telegram messaging service / Telegram 消息服务
│   │   ├── ai_service.py      # AI summary generation service / AI 摘要生成服务
│   └── utils
│       └── config.py          # Configuration management / 配置管理
├── requirements.txt          # Python dependencies / Python 依赖列表
├── README.md                 # Project documentation / 项目文档
└── .github/workflows         # GitHub Actions workflows / GitHub Actions 工作流
```

---

## 🛠 Installation / 安装

### 1️⃣ Clone the repository / 克隆仓库
```bash
git clone <repository-url>
cd daily_market_bot
```

### 2️⃣ Install dependencies / 安装依赖
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables / 配置环境变量
Create a `.env` file in the project root directory and fill in the following:  
在项目根目录创建 `.env` 文件，并填写以下内容：
```properties
FINNHUB_API_KEY=<your_finnhub_api_key>
BOT_TOKEN=<your_telegram_bot_token>
CHAT_ID=<your_telegram_chat_id>
LLM_API_TOKEN=<your_llm_api_token>
DEBUG_MODE=false
```

---

## 🚀 Usage / 使用

### Manual Execution / 手动运行
```bash
python src/main.py
```

### Scheduled Execution / 定时运行
The project includes GitHub Actions workflows to run the script and send daily market briefings automatically.  
项目包含 GitHub Actions 工作流，可定时运行脚本并发送每日市场简报。

---

## 🔧 Configure GitHub Actions / 配置 GitHub Actions

1️⃣ Add the following Secrets in your GitHub repository:  
在 GitHub 仓库中添加以下 Secrets：
- `FINNHUB_API_KEY`
- `BOT_TOKEN`
- `CHAT_ID`
- `LLM_API_TOKEN`

2️⃣ Push the code to GitHub, and the workflows will run automatically.  
推送代码到 GitHub，工作流将自动运行。

---

## 📅 Scheduled Tasks / 定时任务

GitHub Actions workflows will run daily at 0:00 UTC to send market briefings.  
GitHub Actions 工作流会每天 UTC 时间 0:00 自动运行并发送市场简报。

---

## 📜 License / 许可证

This project is licensed under the [MIT License](LICENSE).  
本项目使用 [MIT License](LICENSE)。