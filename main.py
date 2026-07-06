from flask import Flask, request
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__)

# --- دوال المهام التلقائية ---
def job_welcome():
    print("إرسال رسالة ترحيبية دورية للدردشة...")
    # هنا ستضع دالة الإرسال لـ Kick لاحقاً

def job_subscribe():
    print("إرسال رسالة تذكير بالاشتراك المدفوع...")

def job_hype():
    print("إرسال رسالة حماسية للمشاهدين!")

# --- ضبط الجدول الزمني ---
scheduler = BackgroundScheduler()
scheduler.add_job(job_welcome, 'interval', minutes=5)
scheduler.add_job(job_subscribe, 'interval', minutes=15)
scheduler.add_job(job_hype, 'interval', minutes=10)
scheduler.start()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get('event') == 'chat_message':
        content = data.get('data', {}).get('content', '').lower()
        sender = data.get('data', {}).get('sender', {}).get('username', 'صديقي')
        
        # الردود التلقائية
        if any(word in content for word in ["مرحبا", "اهلا", "أهلاً"]):
            print(f"البوت يرد على {sender}: أهلاً بك! نورت البث.")
            
        elif any(word in content for word in ["السلام عليكم", "السلام"]):
            print(f"البوت يرد على {sender}: وعليكم السلام ورحمة الله وبركاته.")

    return "Received", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
