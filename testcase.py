from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo WebDriver (đảm bảo đã cài đặt ChromeDriver)
driver = webdriver.Chrome()

try:
    # 1. Mở Wikipedia
    driver.get("https://www.wikipedia.org/")

    # 2. Tìm ô nhập tìm kiếm
    search_box = driver.find_element(By.NAME, "search")

    # 3. Nhập từ khóa cần tìm
    search_box.send_keys("Selenium (software)")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Chờ trang tải xong

    # 4. Kiểm tra tiêu đề trang có chứa từ khóa không
    if "Selenium (software)" in driver.title:
        print("Test Passed: Kết quả tìm kiếm chính xác!")
    else:
        print("Test Failed: Kết quả không đúng!")

finally:

    # 5. Đóng trình duyệt
    time.sleep(10)
    driver.quit()