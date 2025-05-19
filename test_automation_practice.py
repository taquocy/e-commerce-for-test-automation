from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#  Khởi tạo trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Truy cập trang web
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Chờ trang tải hoàn toàn
wait = WebDriverWait(driver, 10)

#  Xóa iframe quảng cáo nếu có
ads = driver.find_elements(By.CSS_SELECTOR, "iframe[id^='google_ads_iframe']")
for ad in ads:
    driver.execute_script("arguments[0].remove();", ad)

#  2️ Nhập thông tin vào form
driver.find_element(By.ID, "firstName").send_keys("Hoàng Ngọc")
driver.find_element(By.ID, "lastName").send_keys("Bảo Long")
driver.find_element(By.ID, "userEmail").send_keys("long104339@donga.edu.vn")

# 🛠 Cuộn xuống radio button trước khi click
male_radio = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
driver.execute_script("arguments[0].scrollIntoView(true);", male_radio)
wait.until(EC.element_to_be_clickable(male_radio)).click()

# Nhập số điện thoại
driver.find_element(By.ID, "userNumber").send_keys("0123456789")

# Nhập ngày sinh
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.click()

# Chọn tháng và năm
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text("October")
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_visible_text("2005")

# Chọn ngày 18
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--018')]").click()

# Nhập môn học
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Chọn sở thích "Sports"
driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]").click()

# Tải lên ảnh
image_path = r"E:\KTPM2\e-commerce-for-test-automation\tests\test_image.png"
driver.find_element(By.ID, "uploadPicture").send_keys(image_path)

# Nhập địa chỉ
driver.find_element(By.ID, "currentAddress").send_keys("Huế")

# Chọn State
state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state.send_keys("NCR")
state.send_keys(Keys.RETURN)

# Chọn City
city = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)

#  3️ Nhấn Submit
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

#  4️ Kiểm tra kết quả
try:
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))).text
    assert success_message == "Thanks for submitting the form", " Form không được gửi thành công!"
    print(" Test Passed: Form đã gửi thành công!")
except Exception as e:
    print(" Test Failed: Không tìm thấy thông báo xác nhận!", e)

# Đợi 3 giây rồi đóng trình duyệt
driver.quit()
