from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_failed_test(username, password):
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/login")
    time.sleep(2)

    # Điền thông tin đăng nhập
    browser.find_element(By.ID, "userName").send_keys(username)
    time.sleep(1)
    browser.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    # Nhấn nút "Login"
    browser.find_element(By.ID, "login").click()
    time.sleep(3)

    try:
        # Kiểm tra nếu có thông báo lỗi
        error_message = browser.find_element(By.ID, "name")
        print(f"✅ Đăng nhập thất bại đúng như mong đợi! Thông báo lỗi: {error_message.text}")
    except:
        print("❌ Không tìm thấy thông báo lỗi, có thể đã đăng nhập thành công!")

    browser.quit()

# Test với tài khoản sai
login_failed_test("an", "saimatkhau")  # Sai mật khẩu
login_failed_test("hoang", "hoang555") # Sai tài khoản
