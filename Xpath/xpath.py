from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo ChromeDriver
driver = webdriver.Chrome()

try:
    # Truy cập trang chủ hoặc trang chuyên mục của báo Thanh Niên
    driver.get("https://thanhnien.vn/")  # Hoặc một URL khác tùy mục tiêu crawl
    time.sleep(2)  # Chờ trang tải

    # Lấy các tiêu đề chuyên mục với class 'box-category-link-title' (dùng XPath)
    elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'box-category-link-title')]")

    print("🔍 Danh sách chuyên mục:")
    for el in elements:
        title = el.text
        link = el.get_attribute("href")
        print(f"👉 {title} | {link}")

finally:
    driver.quit()