# daily_market_bot

This project is a daily market bot that retrieves and shares cryptocurrency prices and financial news on Twitter. It utilizes various APIs to gather data and automate the tweeting process.

## Features

- Fetches real-time cryptocurrency prices for Bitcoin and Ethereum.
- Retrieves the latest financial news articles.
- Automatically posts updates to Twitter with market data and news.
- **Supports scheduled execution via GitHub Actions.**

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd daily_market_bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys in the `.env` file.

## Usage

Run the application manually using:
```
python src/main.py
```

### Scheduled Execution

This project includes a GitHub Actions workflow to run the bot daily at 8:00 UTC. To enable this:

1. Add your API keys as GitHub Secrets:
   - `API_KEY`
   - `API_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_TOKEN_SECRET`
   - `DEBUG_MODE`
   - `BOT_TOKEN`
   - `CHAT_ID`
   - `LLM_API_TOKEN`

2. Push the repository to GitHub. The workflow will automatically execute based on the schedule defined in `.github/workflows/schedule_tweet.yml` or `.github/workflows/test_tweet.yml`.