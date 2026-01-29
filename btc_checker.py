import requests
import time

def get_bitcoin_price():
    # URL API CoinGecko (Gratis, tidak perlu API Key)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        # Mengirim request ke API
        response = requests.get(url, params=params)
        response.raise_for_status() # Cek jika ada error koneksi
        data = response.json()

        # Mengambil data spesifik
        btc_price = data["bitcoin"]["usd"]
        btc_change = data["bitcoin"]["usd_24h_change"]

        # Menampilkan hasil
        print("Bitcoin Price Report")
        print("====================")
        print(f"Price:      ${btc_price:,.2f} USD")
        print(f"24h Change: {btc_change:+.2f}%")
        
        return btc_price

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_bitcoin_price()
