from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Amjad's Bot is online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # مجرد استقبال للبيانات لنتأكد أن السيرفر يعمل
    data = request.json
    print("وصلت بيانات من Kick!")
    return "Received", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
