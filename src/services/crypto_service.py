import requests

class CryptoService:
    def get_crypto_prices(self):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
        r = requests.get(url).json()
        btc = r["bitcoin"]
        eth = r["ethereum"]
        return btc["usd"], btc["usd_24h_change"], eth["usd"], eth["usd_24h_change"]
