from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import datetime
import time

# --- Cấu hình ---
URL_CRAWL = "https://batdongsan.com.vn/nha-dat-ban-da-nang"
MAX_PAGE = 3  # Thay vì 303 để test nhanh

DEBUG_MODE = True

# --- Khởi tạo WebDriver ---
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(6)

# --- Kết nối MySQL ---
try:
    print(' Kết nối Database...')
    connection = mysql.connector.connect(
        host='localhost',
        database='bds_crawl' if not DEBUG_MODE else 'bds_test',
        user='root',
        password='Y649394$'
    )
    cursor = connection.cursor()
    print(" Kết nối thành công!")

    # --- Lặp qua từng trang ---
    for page in range(1, MAX_PAGE + 1):
        print(f"\n Đang thu thập dữ liệu từ trang {page}...")
        driver.get(f"{URL_CRAWL}/p{page}")
        time.sleep(3)  # Đợi load trang

        # Lấy danh sách bài đăng
        listItem = driver.find_elements(By.CSS_SELECTOR, '.js__product-link-for-product-id')
        print(f"🔍 Tìm thấy {len(listItem)} bài đăng trên trang {page}")

        for item in listItem:
            try:
                title = item.find_element(By.CSS_SELECTOR, '.js__card-title').text
                price = item.find_element(By.CSS_SELECTOR, '.re__card-config-price').text
                distCity = item.find_element(By.CSS_SELECTOR, '.re__card-location').text
                productArea = item.find_element(By.CSS_SELECTOR, '.re__card-config-area').text
                description = ""

                # Lấy thời gian đăng bài
                try:
                    uptime = item.find_element(By.CSS_SELECTOR, '.re__card-published-info span.re__card-published-info-published-at').get_attribute('aria-label')
                except NoSuchElementException:
                    uptime = datetime.date.today()

                print(f" {title} - {price} - {distCity} - {productArea} - {uptime}")

                # Chèn vào database
                sql = """INSERT INTO BATDONGSAN (title, description, image, uptime, price, distcity, space) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (title, description, "", uptime, price, distCity, productArea))
                connection.commit()

            except NoSuchElementException:
                print(" Lỗi khi lấy dữ liệu bài đăng")
                continue

    print(" Thu thập dữ liệu hoàn tất!")

except mysql.connector.Error as error:
    print(f" Lỗi MySQL: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print(" Đã đóng kết nối MySQL")

    driver.quit()
    print(" Đã đóng trình duyệt")
