from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Cấu hình Chrome để tắt GPU và tránh lỗi
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Tắt GPU để tránh lỗi
chrome_options.add_argument("--disable-software-rasterizer")  # Tắt rasterization bằng phần mềm
chrome_options.add_argument("--no-sandbox")  # Tránh lỗi sandbox trên Linux (nếu có)

# Khởi tạo trình duyệt với options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Đợi 3 giây để trang load
time.sleep(3)

# Nhập First Name
first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name.send_keys("Tien")

# Nhập Last Name
last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name.send_keys("Nguyen")

# Nhập Email
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.send_keys("tien@example.com")

# Chọn giới tính (Male)
gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
gender.click()

# Nhập số điện thoại
phone = driver.find_element(By.XPATH, "//input[@id='userNumber']")
phone.send_keys("0123456789")

# Chọn ngày sinh
dob = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
dob.click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']").send_keys("March")
driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']").send_keys("2000")
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]").click()

# Nhập Subject
subject = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Chọn Hobbies (Sports & Reading)
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']").click()

# Upload file ảnh
upload = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
upload.send_keys(r"C:\Users\VAN TIEN\Pictures\Screenshots\gggg.png")

# Nhập địa chỉ hiện tại
address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
address.send_keys("123 Đắk Lắk, Việt Nam")

# Chọn State & City
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
state = driver.find_element(By.XPATH, "//div[@id='state']")
state.click()
driver.find_element(By.XPATH, "//div[text()='NCR']").click()

city = driver.find_element(By.XPATH, "//div[@id='city']")
city.click()
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

# Bấm nút Submit
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# **Asert**: Kiểm tra form đã submit thành công chưa
time.sleep(15)  # Đợi hiển thị popup
assert "Thanks for submitting the form" in driver.page_source


# Đóng trình duyệt
driver.quit()
