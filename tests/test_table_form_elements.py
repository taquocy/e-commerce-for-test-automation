from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo WebDriver
chrome_driver_path = "path/to/chromedriver"  # Cập nhật đường dẫn ChromeDriver
browser = webdriver.Chrome()
browser.get("https://demoqa.com/automation-practice-form")

# Step 1: Nhập thông tin vào form
browser.find_element(By.ID, "firstName").send_keys("Tran")
browser.find_element(By.ID, "lastName").send_keys("Thanh")
browser.find_element(By.ID, "userEmail").send_keys("tranvinhthanh47@gmail.com")
browser.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
browser.find_element(By.ID, "userNumber").send_keys("0123456789")

# Step 2: Chọn ngày sinh
browser.execute_script("document.getElementById('dateOfBirthInput').value = '14 Mar 2004'")

# Step 3: Nhập môn học
subject_input = browser.find_element(By.ID, "subjectsInput")
subject_input.send_keys("Maths")
subject_input.send_keys(Keys.RETURN)

# Step 4: Chọn sở thích
browser.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()

# Step 5: Tải lên ảnh
browser.find_element(By.ID, "uploadPicture").send_keys("C:\\path\\to\\image.jpg")

# Step 6: Nhập địa chỉ
browser.find_element(By.ID, "currentAddress").send_keys("123 Main Street")

# Step 7: Chọn state & city
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.ID, "react-select-3-input").send_keys("NCR")
browser.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)
time.sleep(1)
browser.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
browser.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

# Step 8: Gửi form
browser.find_element(By.ID, "submit").click()
time.sleep(2)

# Step 9: Kiểm tra dữ liệu gửi thành công
modal_title = browser.find_element(By.ID, "example-modal-sizes-title-lg").text
assert modal_title == "Thanks for submitting the form", "Form submission failed!"

# Đóng trình duyệt
browser.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Khởi tạo WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Đợi trang tải xong
driver.implicitly_wait(10)

def slow_type(element, text, delay=0.1):
    """Hàm nhập văn bản từ từ (0.1s mỗi ký tự)"""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)
    time.sleep(1)

# Nhập First Name
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "firstName"))
)
slow_type(first_name, "Tran Phuoc")

# Nhập Last Name
last_name = driver.find_element(By.ID, "lastName")
slow_type(last_name, "Cuong")

# Nhập Email
email = driver.find_element(By.ID, "userEmail")
slow_type(email, "cuong99571@donga.edu.vnvn")

# Chọn giới tính (Male)
gender_radio = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-1']"))
)
driver.execute_script("arguments[0].click();", gender_radio)
time.sleep(1)

# Nhập số điện thoại
phone = driver.find_element(By.ID, "userNumber")
slow_type(phone, "0123456789")

# Nhập ngày sinh
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.click()
time.sleep(1)
dob.clear()
slow_type(dob, "")
dob.send_keys(Keys.RETURN)

# Chọn sở thích (Hobbies)
hobby_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-2']"))
)
driver.execute_script("arguments[0].click();", hobby_checkbox)
time.sleep(1)

# **Bỏ qua phần chọn Picture**

# Nhập địa chỉ (Current Address)
address = driver.find_element(By.ID, "currentAddress")
slow_type(address, "199 Huy Can, DN")

# Chọn State (Mục đầu tiên)
state_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "react-select-3-input"))
)
state_dropdown.send_keys(Keys.ARROW_DOWN)
state_dropdown.send_keys(Keys.RETURN)
time.sleep(1)

# Chọn City (Mục đầu tiên)
city_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "react-select-4-input"))
)
city_dropdown.send_keys(Keys.ARROW_DOWN)
city_dropdown.send_keys(Keys.RETURN)
time.sleep(1)

# Nhấn nút Submit
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(3)

# Đóng trình duyệt
driver.quit()
