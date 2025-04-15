import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument(r"--user-data-dir=C:\Users\Seksak\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--profile-directory=Default")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    return webdriver.Chrome(options=chrome_options)

def scroll_to_bottom(driver, pause_time=1):
    """Scroll ลงล่างสุดเพื่อโหลดคูปองทั้งหมด"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extract_vouchers(driver):
    url = "https://shopee.co.th/m/avc-fsv-all-vouchers"
    driver.get(url)
    time.sleep(5)

    scroll_to_bottom(driver)  # ✅ โหลดคูปองทั้งหมดก่อนดึงข้อมูล

    vouchers = driver.find_elements(By.CLASS_NAME, "k0zDo2")
    print(f"🧾 พบคูปองทั้งหมด: {len(vouchers)} รายการ\n")
    data = []

    for idx, voucher in enumerate(vouchers, 1):
        print(f"🔍 คูปอง #{idx}")
        try:
            button = voucher.find_element(By.XPATH, './/span[text()="เก็บ"]')
            driver.execute_script("arguments[0].click();", button)
            print("✅ พบปุ่ม 'เก็บ' และทำการคลิกแล้ว")

            # ดึงข้อมูลรายละเอียด
            try:
                title = voucher.find_element(By.CLASS_NAME, "uHDvVC").text.strip()
            except:
                title = ""
            try:
                subtitle = voucher.find_element(By.CLASS_NAME, "J1qFmL").text.strip()
            except:
                subtitle = ""
            try:
                shop = voucher.find_element(By.CLASS_NAME, "GZ_QY_").text.strip()
            except:
                shop = ""
            try:
                condition = voucher.find_element(By.XPATH, './/a[contains(text(),"เงื่อนไข")]').get_attribute("href")
            except:
                condition = ""

            data.append({
                "ชื่อคูปอง": title,
                "คำอธิบาย": subtitle,
                "ชื่อร้านค้า": shop,
                "ลิงก์เงื่อนไข": condition
            })

            time.sleep(1)

        except:
            print("⛔ ไม่มีปุ่ม 'เก็บ' → ข้าม")
            continue

    return data

def save_to_excel(data):
    if data:
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"shopee_voucher_unclaimed_{timestamp}.xlsx"
        df.to_excel(filename, index=False)
        print(f"\n✅ บันทึกไฟล์สำเร็จ: {filename}")
    else:
        print("\n⚠️ ไม่พบข้อมูลคูปองที่ยังไม่เก็บ")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        data = extract_vouchers(driver)
        save_to_excel(data)
    finally:
        driver.quit()
