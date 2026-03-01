import requests
from bs4 import BeautifulSoup
import time

BOT_TOKEN = "8616551125:AAG2GNfl_7_ie5G-hWkrjgISy9D_nSAd3lo"
CHAT_ID = "5261056184"

URLS = {
    "مارس": "https://appointment.mosaicvisa.com/calendar/9?month=2026-03",
    "أفريل": "https://appointment.mosaicvisa.com/calendar/9?month=2026-04"
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_appointments():
    for month, url in URLS.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # البحث عن كل العناصر التي تحتوي على كلمة available
        available_elements = soup.find_all(string=lambda text: "available" in text.lower())
        for elem in available_elements:
            # استخراج الرقم بعد كلمة available
            parts = elem.strip().split()
            if len(parts) == 2 and parts[1].isdigit():
                number = int(parts[1])
                if number > 0:
                    send_telegram(f"🚨 موعد متاح في {month} الآن! ({number} متاح)\n{url}")

while True:
    print("Checking...")
    check_appointments()
    time.sleep(60)  # كل دقيقة
