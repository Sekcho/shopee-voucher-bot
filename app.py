from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

# ใส่ Token และ Secret ของคุณ
LINE_CHANNEL_ACCESS_TOKEN = "WksHN32x84DmuXepOaZmqLELO7Th4KFadwl2mtW/rWVScYdUmtAEodvzp9I3oYXLRnFgVqAA5A2v9PW6/bo6dEzS0gTWen8yjRc2v4/emTzZAJURaLTcG8pPgVhrmgilqnUxYneWOsFrGUqToDwpCwdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "b4aded1a4210a0024f2da1c362d6457f"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
    user_text = event.message.text
    reply = f"คุณพิมพ์ว่า: {user_text}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    app.run(port=5000)
