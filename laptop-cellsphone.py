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
        url = "https://cellphones.com.vn/laptop.html"
        driver.get(url)
        time.sleep(5)  # Chờ trang tải hoàn toàn

        # Lấy danh sách laptop
        laptops = driver.find_elements(By.CSS_SELECTOR, ".product-info")

        for laptop in laptops:
            try:
                name = laptop.find_element(By.CSS_SELECTOR, ".product__name").text.strip()
                price = laptop.find_element(By.CSS_SELECTOR, ".product__price--show").text.strip()
                print(f"{name} : {price}")
            except Exception as e:
                print("Lỗi khi lấy dữ liệu sản phẩm:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_laptops()
