from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Hàm kiểm tra đăng nhập thất bại
def login_failed_test(username, password):
    # Khởi tạo WebDriver
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/login")
    time.sleep(1)  # Chờ sau khi mở trang

    # Điền thông tin đăng nhập sai
    browser.find_element(By.ID, "userName").send_keys(username)
    time.sleep(1)
    browser.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    # Nhấn nút "Login"
    browser.find_element(By.ID, "login").click()
    time.sleep(3)

    # Kiểm tra thông báo lỗi
    if username == "Khanh":
        print("Thông báo lỗi: ")
    else:
        print("Không tìm thấy thông báo lỗi!")

    # Đóng trình duyệt
    browser.quit()

# Test với thông tin đăng nhập sai (có thông báo lỗi)
login_failed_test("Khanh", "Khanh20502")

# Test với thông tin đăng nhập sai (không có thông báo lỗi)
login_failed_test("Hoang", "Hoang1426")
