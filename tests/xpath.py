from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# 1. Trang Text Box - nhập dữ liệu
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Tien Nguyen")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("tien@example.com")
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("123 Đắk Lắk")
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("456 Đà Nẵng")
driver.find_element(By.XPATH, "//button[@id='submit']").click()

time.sleep(2)

# 2. Trang Check Box - chọn checkbox
driver.get("https://demoqa.com/checkbox")
time.sleep(2)

# Mở rộng Home
driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
time.sleep(1)

# Chọn Desktop
driver.find_element(By.XPATH, "(//span[@class='rct-checkbox'])[2]").click()
time.sleep(2)

# 3. Trang Radio Button - chọn radio
driver.get("https://demoqa.com/radio-button")
time.sleep(2)

# Chọn Yes
driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
time.sleep(1)

# Chọn Impressive
driver.find_element(By.XPATH, "//label[@for='impressiveRadio']").click()
time.sleep(2)

# Đóng trình duyệt
driver.quit()
