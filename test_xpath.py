from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Mở trang đăng nhập UDA
    driver.get("https://my.uda.edu.vn/sv/svlogin")
    time.sleep(2)  # Chờ trang tải

    # Đọc XPath từ file
    xpath_dict = {}
    with open("uda_xpath.txt", "r", encoding="utf-8") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split(" = ")
                xpath_dict[key] = value

    # Nhập tên đăng nhập
    username = driver.find_element(By.XPATH, xpath_dict["username_field"])
    username.send_keys("12345")  # Thay bằng mã sinh viên thực tế

    # Nhập mật khẩu
    password = driver.find_element(By.XPATH, xpath_dict["password_field"])
    password.send_keys("12345")  # Thay bằng mật khẩu thực tế

    # Bấm nút đăng nhập
    login_button = driver.find_element(By.XPATH, xpath_dict["login_button"])
    login_button.click()

    # Chờ tải trang (tùy chỉnh nếu cần)
    time.sleep(3)

    # Kiểm tra lỗi đăng nhập
    try:
        error_message = driver.find_element(By.XPATH, xpath_dict["error_message"]).text
        print(f"Lỗi đăng nhập: {error_message}")
    except:
        print(" Đăng nhập thành công!")

finally:
    driver.quit()  # Đóng trình duyệt
