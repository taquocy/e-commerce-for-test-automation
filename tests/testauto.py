from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Cài đặt trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Mở trang web
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(2)  # Chờ trang tải xong

# Điền thông tin vào các trường

driver.find_element(By.ID, "firstName").send_keys("Nguyen")
driver.find_element(By.ID, "lastName").send_keys("Luong Hai Dang")
driver.find_element(By.ID, "userEmail").send_keys("nguyenluonghaidang@example.com")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys("0123456789")

driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2000")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("June")
driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)

driver.find_element(By.XPATH, "//label[text()='Sports']").click()

driver.find_element(By.ID, "currentAddress").send_keys("33 XoViet Street, DaNang, Vietnam")

# Chọn State và City
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID, "state").click()
driver.find_element(By.XPATH, "//div[text()='NCR']").click()
driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

# Bấm nút Submit
driver.find_element(By.ID, "submit").click()

time.sleep(3)  # Chờ kết quả hiển thị

driver.quit()