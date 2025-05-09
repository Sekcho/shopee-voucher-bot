import os
from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import subprocess
import glob

# โหลดตัวแปรจาก .env
load_dotenv()

app = Flask(__name__)

# ดึงค่าจาก .env
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

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
    msg = event.message.text.strip().lower()

    if msg in ["เก็บโค้ด", "เก็บคูปอง", "ดึงคูปอง"]:
        result = run_script_and_get_image()
        if result:
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=result,
                    preview_image_url=result
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="⚠️ ไม่มีคูปองใหม่ให้เก็บในตอนนี้")
            )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"คุณพิมพ์ว่า: {msg}")
        )

def run_script_and_get_image():
    try:
        subprocess.run(["python", "main.py"], check=True)

        files = glob.glob("shopee_coupon_summary_*.png")
        if not files:
            return None

        latest_file = max(files, key=os.path.getctime)
        public_url = upload_to_static_and_get_url(latest_file)
        return public_url
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None

def upload_to_static_and_get_url(file_path):
    """จำลองการส่งไฟล์ผ่าน LINE ด้วย URL แบบ localhost/ngrok"""
    ngrok_base = "https://your-ngrok-url.ngrok-free.app/static"  # เปลี่ยนตรงนี้ถ้ามี ngrok URL จริง
    static_dir = os.path.join(os.getcwd(), "static")
    os.makedirs(static_dir, exist_ok=True)

    destination = os.path.join(static_dir, os.path.basename(file_path))
    os.replace(file_path, destination)

    return f"{ngrok_base}/{os.path.basename(file_path)}"

if __name__ == "__main__":
    app.run(port=5000)
