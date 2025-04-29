from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Khởi động Chrome
driver = webdriver.Chrome(service=Service("chromedriver"))

# Mở trang demo
driver.get("https://demoqa.com/text-box")

# Điền thông tin vào form
driver.find_element(By.ID, "userName").send_keys("Nguyen Van A")
driver.find_element(By.ID, "userEmail").send_keys("vana@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Đường A, Quận B, TP.HCM")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Đường B, Quận C, Hà Nội")

# Click nút Submit
driver.find_element(By.ID, "submit").click()

# Đợi 2s để xem kết quả
time.sleep(2)

# Đóng trình duyệt
driver.quit()
