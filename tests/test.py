from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Nếu dùng Firefox: webdriver.Firefox()
driver.maximize_window()

# Step 1: Mở trang chứa form
driver.get("https://demoqa.com/text-box")  # Thay bằng URL thực tế của form
time.sleep(2)  # Chờ trang tải xong

# Step 2: Nhập dữ liệu vào form
full_name = "Tran Tri Kien"
email = "kien100633@donga.edu.vn"
current_address = "123 ABC Street, Ho Chi Minh City"
permanent_address = "456 XYZ Avenue, Hanoi"

# Nhập Full Name
driver.find_element(By.XPATH, "//*[@id='userName']").send_keys(full_name)

# Nhập Email
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys(email)

# Nhập Current Address
driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys(current_address)

# Nhập Permanent Address
driver.find_element(By.XPATH, "//*[@id='permanentAddress']").send_keys(permanent_address)

time.sleep(1)

# Step 3: Nhấn Submit
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(2)  # Chờ hệ thống phản hồi

# Step 4: Kiểm tra dữ liệu hiển thị
output_name = driver.find_element(By.XPATH, "//p[@id='name']").text
output_email = driver.find_element(By.XPATH, "//p[@id='email']").text
output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddressOutput']").text
output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddressOutput']").text

# Kiểm tra dữ liệu đầu ra khớp với đầu vào
assert full_name in output_name, "Test Failed: Full Name không khớp!"
assert email in output_email, "Test Failed: Email không khớp!"
assert current_address in output_current_address, "Test Failed: Current Address không khớp!"
assert permanent_address in output_permanent_address, "Test Failed: Permanent Address không khớp!"

print("Test Passed: Dữ liệu nhập và hiển thị chính xác!")

# Đóng trình duyệt
driver.quit()
