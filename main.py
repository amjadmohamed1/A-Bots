import os
import requests
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# جلب البيانات من المتغيرات التي أضفتها
CHANNEL_ID = os.environ.get('KICK_CHANNEL_ID')
API_TOKEN = os.environ.get('KICK_CLIENT_SECRET') # سنستخدم السيكريت كتوكن مبدئي

def send_chat_message(message):
    url = f"https://kick.com/api/v1/channels/{CHANNEL_ID}/messages"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"content": message}
    try:
        requests.post(url, headers=headers, json=payload)
    except Exception as e:
        print(f"Error: {e}")

# المهام الدورية
scheduler = BackgroundScheduler()
scheduler.add_job(lambda: send_chat_message("أهلاً يا أساطير !"), 'interval', minutes=5)
scheduler.add_job(lambda: send_chat_message("يا مطنوخ، لا تنسى الاشتراك المدفوع!"), 'interval', minutes=15)
scheduler.add_job(lambda: send_chat_message("من جاهز ينزل معنا في الجولة القادمة؟"), 'interval', minutes=10)
scheduler.start()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and data.get('event') == 'chat_message':
        content = data.get('data', {}).get('content', '').lower()
        if "مرحبا" in content or "اهلا" in content:
            send_chat_message("أهلاً بك! نورت البث.")
        elif "السلام" in content:
            send_chat_message("وعليكم السلام ورحمة الله.")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
