from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình trình duyệt
options = Options()
options.add_argument("--start-maximized")

# Đường dẫn tới chromedriver
service = Service(executable_path="chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://demoqa.com/automation-practice-form")

    wait = WebDriverWait(driver, 10)

    # Đóng quảng cáo footer nếu có
    try:
        driver.execute_script("document.getElementById('fixedban').style.display='none'")
    except:
        pass

    # Điền Họ và Tên
    driver.find_element(By.ID, "firstName").send_keys("Nguyen")
    driver.find_element(By.ID, "lastName").send_keys("Van A")

    # Email
    driver.find_element(By.ID, "userEmail").send_keys("vana@example.com")

    # Giới tính
    driver.find_element(By.XPATH, "//label[text()='Male']").click()

    # Số điện thoại
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")

    # Ngày sinh
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1995")
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("May")
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()  # Chọn ngày 15

    # Môn học
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys("Maths")
    subject_input.send_keys("\n")  # Chọn gợi ý

    # Sở thích
    driver.find_element(By.XPATH, "//label[text()='Reading']").click()

    # Upload ảnh
    file_input = driver.find_element(By.ID, "uploadPicture")
    file_input.send_keys("D:\\path\\to\\your\\image.jpg")  # Thay đường dẫn thực tế

    # Địa chỉ
    driver.find_element(By.ID, "currentAddress").send_keys("123 Đường ABC, Quận 1, TP.HCM")

    # Chọn State và City
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll xuống
    driver.find_element(By.ID, "react-select-3-input").send_keys("NCR\n")
    driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi\n")

    # Submit
    driver.find_element(By.ID, "submit").click()

    # Đợi Modal hiện ra và in nội dung
    wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    print("==> Form đã được gửi thành công!")

    # Optional: đóng modal
    driver.find_element(By.ID, "closeLargeModal").click()

finally:
    time.sleep(3)
    driver.quit()
