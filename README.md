# daily_market_bot

This project is a daily market bot that retrieves and shares cryptocurrency prices and financial news on Twitter. It utilizes various APIs to gather data and automate the tweeting process.

## Project Structure

```
daily_market_bot
├── src
│   ├── main.py               # Entry point of the application
│   ├── services              # Contains service modules for different functionalities
│   │   ├── twitter_service.py # Handles interactions with the Twitter API
│   │   ├── crypto_service.py  # Fetches cryptocurrency data from CoinGecko API
│   │   └── news_service.py    # Retrieves financial news from Finnhub API
│   └── utils
│       └── config.py         # Manages configuration and API keys
├── requirements.txt          # Lists required Python libraries and dependencies
└── README.md                 # Project documentation
```

## Features

- Fetches real-time cryptocurrency prices for Bitcoin and Ethereum.
- Retrieves the latest financial news articles.
- Automatically posts updates to Twitter with market data and news.

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

Run the application using:
```
python src/main.py
```

This will trigger the bot to fetch the latest cryptocurrency prices and financial news, and post them to Twitter.