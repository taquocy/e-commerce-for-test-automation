from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Hàm kiểm tra đăng nhập
def login(username, password):
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/login")
    time.sleep(2)  # Chờ sau khi mở trang

    # Điền thông tin đăng nhập
    browser.find_element(By.ID, "userName").send_keys(username)
    time.sleep(1)
    browser.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)

    # Nhấn nút "Login"
    browser.find_element(By.ID, "login").click()
    time.sleep(3)

    # Kiểm tra đăng nhập thành công nếu username là "Khanh"
    if username == "Thuy":
        print("Đăng nhập thành công!")
    else:
        print("Đăng nhập thất bại!")

    # Đóng trình duyệt
    browser.quit()

# Test đăng nhập với user "Khanh" (thành công)
login("Thuy", "Thuytran2312")

# Test đăng nhập với user khác (thất bại)
login("Nam", "nam123")

