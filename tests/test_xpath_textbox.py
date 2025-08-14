from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

# Tìm các phần tử bằng XPath và nhập dữ liệu
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Tien Nguyen")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("tien@example.com")
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("123 Đắk Lắk, Việt Nam")
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("456 Đà Nẵng, Việt Nam")

# Nhấn nút Submit
driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Chờ một lúc để xem kết quả
time.sleep(15)

# Đóng trình duyệt
driver.quit()
