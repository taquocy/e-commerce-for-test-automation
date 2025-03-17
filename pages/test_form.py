from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Step 1: Nhập First Name
print("Step 1: Nhập First Name")
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Ngo")

# Step 2: Nhập Last Name
print("Step 2: Nhập Last Name")
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Quoc Khanh")   

# Step 3: Nhập Email
print("Step 3: Nhập Email")
email = driver.find_element(By.ID, "userEmail")
email.send_keys("khanh104087@donga.edu.vn.com")

# Step 4: Chọn giới tính
print("Step 4: Chọn giới tính")
gender = driver.find_element(By.XPATH, "//label[text()='Male']")
gender.click()

# Step 5: Nhập số điện thoại
print("Step 5: Nhập số điện thoại")
phone = driver.find_element(By.ID, "userNumber")
phone.send_keys("0123456789")

# Step 6: Chọn ngày sinh (Xóa iframe quảng cáo trước)
print("Step 6: Chọn ngày sinh")
try:
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.execute_script("arguments[0].remove();", iframe)  # Xóa iframe quảng cáo
    print("Đã loại bỏ iframe quảng cáo.")
except:
    print("Không tìm thấy iframe quảng cáo, tiếp tục chạy script.")

# Cuộn trang đến phần tử Date of Birth Input
dob = driver.find_element(By.ID, "dateOfBirthInput")
driver.execute_script("arguments[0].scrollIntoView();", dob)

# Chờ đến khi có thể click vào ô nhập ngày sinh
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))).click()

# Chọn năm sinh
year = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'react-datepicker__year-select')]"))
)
year.click()
year_option = driver.find_element(By.XPATH, "//option[text()='2000']")
year_option.click()

# Chọn tháng sinh
month = driver.find_element(By.XPATH, "//select[contains(@class,'react-datepicker__month-select')]")
month.click()
month_option = driver.find_element(By.XPATH, "//option[text()='January']")
month_option.click()

# Chọn ngày sinh
day = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']")
day.click()

# Step 7: Chọn Subject
print("Step 7: Chọn Subject")
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Step 8: Chọn Hobbies
print("Step 8: Chọn Hobbies")
hobby = driver.find_element(By.XPATH, "//label[text()='Sports']")
hobby.click()

# Step 9: Upload file ảnh (nếu cần)
# print("Step 9: Upload file ảnh")
# upload = driver.find_element(By.ID, "uploadPicture")
# upload.send_keys("D:\\path\\to\\your\\image.jpg")  # Thay đổi đường dẫn file

# Step 10: Nhập địa chỉ
print("Step 10: Nhập địa chỉ")
address = driver.find_element(By.ID, "currentAddress")
address.send_keys("123 Đường ABC, Quận XYZ, Thành phố HCM")

# Step 11: Chọn State
print("Step 11: Chọn State")
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.RETURN)

# Step 12: Chọn City
print("Step 12: Chọn City")
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)

# Step 13: Click Submit
print("Step 13: Click Submit")
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit)  # Dùng JavaScript click để tránh lỗi

# Step 14: Xác nhận form đã gửi thành công
print("Step 14: Kiểm tra xác nhận")
modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
assert "Thanks for submitting the form" in modal.text
print("Form đã được submit thành công!")

# Đợi vài giây để xem kết quả
time.sleep(3)

# Đóng trình duyệt
driver.quit()
