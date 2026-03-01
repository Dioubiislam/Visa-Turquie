import requests
import time
from bs4 import BeautifulSoup

BOT_TOKEN = "8616551125:AAG2GNfl_7_ie5G-hWkrjgISy9D_nSAd3lo"
CHAT_ID = "5261056184"

URLS = {
    "مارس": "https://appointment.mosaicvisa.com/calendar/9?month=2026-03",
    "أفريل": "https://appointment.mosaicvisa.com/calendar/9?month=2026-04"
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def check_appointments():
    for month, url in URLS.items():
        response = requests.get(url)
        if "available" in response.text.lower():
            send_telegram(f"🚨 موعد متاح في {month} الآن!\n{url}")
            return True
    return False

while True:
    print("Checking...")
    found = check_appointments()
    time.sleep(60)
