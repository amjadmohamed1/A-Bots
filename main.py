from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ضع رابط الـ API الخاص بـ Kick هنا إذا لزم الأمر، أو استخدم توكن البوت
KICK_API_URL = "https://kick.com/api/v1/..." 

@app.route('/')
def home():
    return "Amjad's Pro Bot is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = data.get('event')

    # 1. الترحيب بالمتابعين
    if event_type == 'follow':
        username = data.get('user', {}).get('name')
        message = f"أهلاً بك يا {username} في جيش Amjad! شكراً على المتابعة!"
        send_chat_message(message)

    # 2. الرد على أوامر الدردشة (مثال: !social)
    elif event_type == 'chat_message':
        content = data.get('content', '')
        if content.lower() == '!social':
            send_chat_message("تابعوني على حساباتي: TikTok, Kick, و YouTube!")
            
    return "Received", 200

def send_chat_message(message):
    # هنا يتم وضع كود الاتصال بـ API الخاص بـ Kick لإرسال الرسالة
    print(f"إرسال إلى الدردشة: {message}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
