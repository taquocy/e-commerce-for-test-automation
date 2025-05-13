from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Dữ liệu nhập
form_data = {
    "firstName": "Vo Hoai Giang",
    "lastName": "Test",
    "email": "hehe@gmail.com",
    "phone": "0797955555"
}

try:
    # Mở trang web
    driver.get("https://demoqa.com/automation-practice-form")
    
    # Đợi tối đa 10 giây cho mỗi phần tử
    wait = WebDriverWait(driver, 10)

    # Điền First Name
    first_name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']")))
    first_name_field.send_keys(form_data["firstName"])

    # Điền Last Name
    last_name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='lastName']")))
    last_name_field.send_keys(form_data["lastName"])

    # Điền Email
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userEmail']")))
    email_field.send_keys(form_data["email"])

    # Điền Mobile Number
    phone_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userNumber']")))
    phone_field.send_keys(form_data["phone"])

    # Chụp ảnh màn hình sau khi điền xong form
    driver.save_screenshot("form_filled.png")
    print("✅ Form đã được điền và ảnh chụp đã lưu.")

except TimeoutException as e:
    print("❌ Không tìm thấy một phần tử nào đó trong thời gian cho phép:", e)

finally:
    # Tạm dừng để xem kết quả (tuỳ chọn)
    time.sleep(2)

    # Đóng trình duyệt
    driver.quit()
