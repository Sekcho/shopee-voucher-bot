# 📦 Shopee Voucher Bot (LINE Integration)

โปรเจกต์นี้ช่วยให้คุณสามารถ **เก็บคูปอง Shopee อัตโนมัติ** ผ่าน LINE Bot ได้ทันที  
โดยไม่ต้องเปิดเบราว์เซอร์ด้วยตัวเอง ✨

---

## ✅ คุณสมบัติ (Features)

- 🧠 เก็บเฉพาะคูปองที่ยังไม่เคยกด (ดูจากปุ่ม “เก็บ”)
- 📊 สรุปรายงานคูปองแบบกราฟ ส่งกลับทาง LINE
- 🔐 เก็บ Token และ Secret แบบปลอดภัยใน `.env`
- 🌐 รองรับการใช้งานผ่าน ngrok / localhost

---

## 🛠️ วิธีใช้งาน

1. **ตั้งค่า Line Developer**
   - สร้าง Channel ใหม่ → เปิด Webhook → ตั้งค่า ngrok URL `/callback`

2. **แก้ไขไฟล์ `.env`**
```env
LINE_CHANNEL_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
LINE_CHANNEL_SECRET=YOUR_CHANNEL_SECRET
NGROK_BASE_URL=https://xxxxx.ngrok-free.app
```

3. **ติดตั้ง dependencies**
```bash
pip install -r requirements.txt
```

4. **รัน Flask (LINE webhook)**
```bash
python app_final.py
```

5. **รันผ่าน LINE → พิมพ์ว่า**: `เก็บคูปอง`

---

## 📁 โครงสร้างโปรเจกต์

```
web_automation_bot/
├── main.py                # ดึงคูปอง Shopee และบันทึกเป็นไฟล์ + กราฟ
├── app_final.py           # LINE Bot webhook สำหรับตอบกลับ
├── .env                   # LINE Secret (ไม่ควรแชร์)
├── static/                # เก็บภาพสรุปกราฟเพื่อส่งกลับ
├── data/                  # เก็บไฟล์ CSV
├── utils.py               # ฟังก์ชันช่วยจัดการกราฟ
├── requirements.txt
└── README.md
```

---

## 💡 แรงบันดาลใจ

"เริ่มจากการเก็บคูปอง Shopee ทุกวัน จนอยากให้ระบบทำแทน"  
จึงเกิดไอเดียพัฒนา Automation Bot + LINE สำหรับใช้งานง่ายขึ้น

---

พัฒนาโดย ❤️: [@Sekcho](https://github.com/sekcho)