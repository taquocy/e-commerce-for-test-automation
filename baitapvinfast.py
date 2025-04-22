from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import mysql.connector

def convert_price(price_str):
    return int(price_str.replace(".", "").replace(" đ", ""))
# Thông tin kết nối đến CSDL trên db4free.net
DB_CONFIG = {
    "host": "db4free.net",
    "user": "taquocy",
    "password": "Y649394$y",
    "database": "batdongsandanang"
}


def insert_car_data(car_list):
    try:
        # Kết nối đến MySQL
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Câu lệnh SQL để chèn dữ liệu
        sql = "INSERT INTO XeMay (Ten, Gia) VALUES (%s, %s)"

        # Chèn dữ liệu
        cursor.executemany(sql, car_list)
        conn.commit()
        print(f"Đã chèn {cursor.rowcount} xe vào database.")

    except mysql.connector.Error as err:
        print(f"Lỗi: {err}")
    finally:
        cursor.close()
        conn.close()

# Khởi tạo trình duyệt Chrome
def get_vinfast_cars():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Chạy ẩn để không mở cửa sổ trình duyệt
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://xe.chotot.com/cua-hang-chinh-hang/vinfast-official"
    driver.get(url)
    time.sleep(5)  # Chờ trang tải xong

    cars = driver.find_elements(By.CSS_SELECTOR, ".peud91t")

    car_list = []
    for car in cars:
        try:
            name = car.find_element(By.CSS_SELECTOR, ".p15mzs6m").text
            price = car.find_element(By.CSS_SELECTOR, ".p1wl2ldn").text
            price_number = convert_price(price)

            car_list.append((name, price_number))
            print(f"Tên xe: {name} - Giá: {price}")
        except:
            continue

    driver.quit()
    return car_list


# Gọi hàm chèn dữ liệu
if __name__ == "__main__":
    car_data = get_vinfast_cars()
    if car_data:
        insert_car_data(car_data)
