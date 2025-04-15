# 🤖 Shopee Voucher Automation Bot

ระบบนี้ช่วยให้คุณสามารถ **เก็บคูปอง Shopee อัตโนมัติ** และรับรายงานผลผ่าน LINE Bot พร้อมแสดงผลในรูปแบบกราฟ

---

## 📌 ฟีเจอร์หลัก

- ✅ เก็บคูปอง Shopee ที่ยังไม่ได้เก็บ (เฉพาะหน้า [All Vouchers](https://shopee.co.th/m/avc-fsv-all-vouchers))
- ✅ สรุปรายงานคูปองใหม่ที่เก็บในรูปแบบ **Excel**
- ✅ แสดงผลสรุปคูปองในรูปแบบ **กราฟภาพ**
- ✅ เชื่อมต่อ **LINE Bot** เพื่อสั่งงานและรับรายงานได้
- ✅ รองรับหลายบัญชี (ในอนาคต รองรับหลาย Chrome Profile)

---

## 🚀 วิธีเริ่มต้นใช้งาน

```bash
git clone https://github.com/your-username/web_automation_bot.git
cd web_automation_bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app_final.py
```

> 🧪 ก่อนใช้งาน: ให้เปิด Chrome โปรไฟล์ของคุณ และ Login Shopee ค้างไว้

---

## 🤖 คำสั่งผ่าน LINE Bot

| คำสั่ง LINE | ผลลัพธ์ |
|-------------|----------|
| `เก็บโค้ด` หรือ `เก็บคูปอง` | Bot จะเข้า Shopee → เก็บคูปอง → ส่งกราฟรายงานผ่าน LINE |
| คำอื่น ๆ | Bot จะตอบกลับข้อความปกติ |

---

## 🧠 โฟลว์ระบบ

1. ผู้ใช้พิมพ์คำสั่งใน LINE
2. Flask app รับ Webhook → เรียกใช้ `main.py`
3. ระบบใช้ Selenium ดึงคูปองใหม่ พร้อมคลิกปุ่ม "เก็บ"
4. บันทึกข้อมูลลง Excel และสร้างกราฟด้วย Matplotlib
5. Bot ส่งรูปกราฟกลับไปยังผู้ใช้

---

## 📁 โครงสร้างโปรเจกต์

```
web_automation_bot/
│
├── main.py              # ดึงคูปอง Shopee + บันทึก Excel
├── app_final.py         # Flask + LINE Bot integration
├── requirements.txt     # Python dependencies
├── data/                # ไฟล์ CSV / Excel ที่สร้าง
├── utils.py             # ฟังก์ชันช่วยสร้างกราฟ
└── README.md
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 🧊 อัปเดตล่าสุด: 2025-04-15
