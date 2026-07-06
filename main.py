import os
import requests
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# جلب البيانات من المتغيرات في Railway
CHANNEL_ID = os.environ.get('KICK_CHANNEL_ID')
API_TOKEN = os.environ.get('KICK_CLIENT_SECRET') 

def send_chat_message(message):
    print(f"محاولة إرسال رسالة: {message}") # للتأكد في الـ Logs

# المهام الدورية
scheduler = BackgroundScheduler()
scheduler.add_job(lambda: send_chat_message("أهلاً يا أساطير!"), 'interval', minutes=5)
scheduler.start()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"بيانات جديدة وصلت من Kick: {data}") # هذا السطر هو الأهم الآن
    
    if data and data.get('event') == 'chat_message':
        content = data.get('data', {}).get('content', '').lower()
        if "مرحبا" in content:
            send_chat_message("أهلاً بك! نورت البث.")
            
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
