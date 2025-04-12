from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_success_test(username, password):
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
        # Kiểm tra xem có phần tử chứa tên người dùng sau khi đăng nhập không
        user_logged_in = browser.find_element(By.ID, "userName-value")
        print(f"✅ Đăng nhập thành công! Chào {user_logged_in.text}.")
    except:
        print("❌ Đăng nhập thất bại!")

    browser.quit()

# Test với tài khoản đúng
login_success_test("an", "antestcode2005")
