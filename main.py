from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "A-Bots is running!"

# هذا هو المسار الذي ستضعه في منصة Kick
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("بيانات جديدة من Kick:", data)
    return "Received", 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
