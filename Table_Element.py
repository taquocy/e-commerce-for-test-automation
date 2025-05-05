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