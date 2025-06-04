from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt (Ví dụ: Chrome)
driver = webdriver.Chrome()

try:
    # Bước 1: Mở trang web
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(2)  # Đợi trang tải

    # Bước 2: Xác định các phần tử trên form
    full_name_input = driver.find_element(By.XPATH, "//*[@id='userName']")
    email_input = driver.find_element(By.XPATH, "//*[@id='userEmail']")
    current_address_input = driver.find_element(By.XPATH, "//*[@id='currentAddress']")
    permanent_address_input = driver.find_element(By.XPATH, "//*[@id='permanentAddress']")
    submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")

    # Bước 3: Nhập dữ liệu vào các trường
    full_name_input.send_keys("Bui Dinh Khoi")
    email_input.send_keys("khoikhoi@example.com")
    current_address_input.send_keys("123 Đường ABC, TP.DNN")
    permanent_address_input.send_keys("456 Đường XYZ, Hà Nội")

    # Bước 4: Nhấn nút Submit
    submit_button.click()
    time.sleep(2)  # Đợi kết quả xử lý

    # Bước 5: Kiểm tra kết quả (Nếu có phần hiển thị lại dữ liệu nhập vào)
    assert "Phạm Minh Toàn" in driver.page_source, "Tên không được hiển thị đúng!"
    assert "khoikhoi@example.com" in driver.page_source, "Email không được hiển thị đúng!"
    assert "123 Đường ABC, TP.DNDN" in driver.page_source, "Current Address không được hiển thị đúng!"
    assert "456 Đường XYZ, Hà Nội" in driver.page_source, "Permanent Address không được hiển thị đúng!"

    print("Test Case Passed!")

except Exception as e:
    print(f"Test Case Failed: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
