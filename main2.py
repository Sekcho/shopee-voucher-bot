from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# ตั้งค่าด้วย Channel Secret และ Channel Access Token ของคุณ
CHANNEL_ACCESS_TOKEN = 'WksHN32x84DmuXepOaZmqLELO7Th4KFadwl2mtW/rWVScYdUmtAEodvzp9I3oYXLRnFgVqAA5A2v9PW6/bo6dEzS0gTWen8yjRc2v4/emTzZAJURaLTcG8pPgVhrmgilqnUxYneWOsFrGUqToDwpCwdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = 'xb4aded1a4210a0024f2da1c362d6457f'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = f"คุณพิมพ์ว่า: {msg}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    app.run(port=5000)
