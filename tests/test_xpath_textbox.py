from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1️⃣ Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()  # Phóng to cửa sổ trình duyệt
driver.get("https://demoqa.com/text-box")

try:
    # 2️⃣ Tìm các phần tử bằng XPath và nhập dữ liệu
    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Tien Nguyen")
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("tien@example.com")
    driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("123 Đắk Lắk, Việt Nam")
    driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("456 Đà Nẵng, Việt Nam")

    # 3️⃣ Cuộn chuột đến nút Submit trước khi click
    submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    # 4️⃣ Chờ đến khi nút có thể click rồi nhấn Submit
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))).click()

    # 5️⃣ Chờ một lúc để xem kết quả
    time.sleep(2)

    # 6️⃣ Kiểm tra dữ liệu có hiển thị đúng không (Assertion)
    output_name = driver.find_element(By.XPATH, "//p[@id='name']").text
    output_email = driver.find_element(By.XPATH, "//p[@id='email']").text

    assert "Tien Nguyen" in output_name, "Tên không đúng!"
    assert "tien@example.com" in output_email, "Email không đúng!"
    print("✅ Test Passed - Dữ liệu hiển thị chính xác!")

except Exception as e:
    print(f"❌ Test Failed - Lỗi: {e}")

finally:
    # 7️⃣ Đóng trình duyệt sau khi kiểm tra xong
    time.sleep(15)
    driver.quit()