import requests

class CryptoService:
    def get_crypto_prices(self):
        # 定义标的物
        assets = ["bitcoin", "ethereum", "solana"]
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(assets)}&vs_currencies=usd&include_24hr_change=true"
        r = requests.get(url).json()
        
        crypto_data = {}
        for asset in assets:
            price = r[asset]["usd"]
            change = r[asset]["usd_24h_change"]
            crypto_data[asset] = (price, change)
        
        return crypto_data
