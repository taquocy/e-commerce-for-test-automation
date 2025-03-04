from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt (ví dụ: Chrome)
driver = webdriver.Chrome()

# Truy cập vào trang web
driver.get("https://e-commerce-for-testing.onrender.com")

# Đăng nhập vào tài khoản admin
email_input = driver.find_element(By.XPATH, "//input[@type='email']")
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

email_input.send_keys("superadmin@gmail.com")
password_input.send_keys("admin123")
login_button.click()

# Chờ đợi một chút để trang Home load xong
time.sleep(5)

# Lấy tất cả các phần tử trên trang Home bằng XPath
elements = driver.find_elements(By.XPATH, "//*")




# In ra thông tin của các phần tử
for element in elements:
    print(f"Tag: {element.tag_name}, Text: {element.text}, ID: {element.get_attribute('id')}, Class: {element.get_attribute('class')}")

# Đóng trình duyệt
driver.quit()