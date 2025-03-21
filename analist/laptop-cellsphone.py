import pyodbc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_laptops():
    # Cấu hình Selenium
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Chạy không hiển thị trình duyệt
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    # Khởi tạo trình duyệt
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Mở trang web
        url = "https://cellphones.com.vn/laptop/mac.html"
        driver.get(url)
        time.sleep(5)  # Chờ trang tải hoàn toàn

        # Lấy danh sách laptop
        laptops = driver.find_elements(By.CSS_SELECTOR, ".product-info")

        for laptop in laptops:
            try:
                name = laptop.find_element(By.CSS_SELECTOR, ".product__name").text.strip()
                price = laptop.find_element(By.CSS_SELECTOR, ".product__price--show").text.strip()
                print(f"{name} : {price}")
                
                insert_laptop();
                
            except Exception as e:
                print("Lỗi khi lấy dữ liệu sản phẩm:", e)

    finally:
        driver.quit()

# kết nối SQL server
def connect_db():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=127.0.0.1;"  # Hoặc IP máy chủ SQL Server
            "DATABASE=analist;"  # Thay bằng database của bạn
            "UID=sa;"  # Thay bằng username của bạn
            "PWD=0838984511Kiena;"  # Thay bằng password của bạn
            "TrustServerCertificate=yes;"
        )
        return conn
    except Exception as e:
        print("❌ Lỗi kết nối SQL Server:", e)
        return None


# chèn dữ liệu vào SQL server
def insert_laptop(name, price):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO laptop_Mac (name, price) VALUES (?, ?)"
            print(f"📌 SQL Query: {sql} | Data: ({name}, {price})")
            cursor.execute(sql, (name, price))
            conn.commit()
            print(f"✅ Đã thêm: {name} - {price}")
        except Exception as e:
            print("❌ Lỗi khi thêm dữ liệu:", e)
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    scrape_laptops()
