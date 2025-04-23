from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Cấu hình Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--no-sandbox")

# Mở trình duyệt
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Đợi load trang
time.sleep(2)

# Nhập Username
username = driver.find_element(By.ID, "username")
username.send_keys("student")

# Nhập Password
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

# Nhấn nút Submit
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()

# Đợi load trang kết quả
time.sleep(3)

# Kiểm tra đăng nhập thành công bằng tiêu đề trang mới
assert "Logged In Successfully" in driver.page_source
print("✅ Đăng nhập thành công!")

# Đóng trình duyệt
driver.quit()