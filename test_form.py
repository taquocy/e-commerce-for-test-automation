from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Step 1: Nhập First Name
first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name.send_keys("Nguyen")

# Step 2: Nhập Last Name
last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name.send_keys("Van A")

# Step 3: Nhập Email
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.send_keys("test@example.com")

# Step 4: Chọn giới tính
gender = driver.find_element(By.XPATH, "//label[text()='Male']")
gender.click()

# Step 5: Nhập số điện thoại
phone = driver.find_element(By.XPATH, "//input[@id='userNumber']")
phone.send_keys("0123456789")

# Step 6: Chọn ngày sinh
dob = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
driver.execute_script("arguments[0].scrollIntoView();", dob)
dob.click()

# Chọn năm
year = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'react-datepicker__year-select')]"))
)
year.click()
driver.find_element(By.XPATH, "//option[text()='2000']").click()

# Chọn tháng
month = driver.find_element(By.XPATH, "//select[contains(@class,'react-datepicker__month-select')]")
month.click()
driver.find_element(By.XPATH, "//option[text()='January']").click()

# Chọn ngày
day = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']")
day.click()

# Step 7: Nhập môn học (Subjects)
subject = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Step 8: Chọn sở thích
hobby = driver.find_element(By.XPATH, "//label[text()='Sports']")
hobby.click()

# Step 9: Nhập địa chỉ
address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
address.send_keys("123 Đường ABC, Quận XYZ, TP HCM")

# Step 10: Chọn State
state = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
state.send_keys("NCR")
state.send_keys(Keys.RETURN)

# Step 11: Chọn City
city = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)

# Step 12: Click Submit
submit = driver.find_element(By.XPATH, "//button[@id='submit']")
driver.execute_script("arguments[0].click();", submit)  # Dùng JavaScript để tránh lỗi click

# Step 13: Kiểm tra xác nhận
modal = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'modal-content')]")))
assert "Thanks for submitting the form" in modal.text
print("✅ Form đã được submit thành công!")

# Đợi vài giây để xem kết quả
time.sleep(3)

# Đóng trình duyệt
driver.quit()