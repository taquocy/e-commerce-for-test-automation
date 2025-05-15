import unittest
import configparser
import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.browser_setup import BrowserSetup  # Nếu bạn dùng class BrowserSetup

class TestTextBox(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini (nếu cần)
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))  

        # Khởi tạo WebDriver
        self.driver = BrowserSetup.get_driver()  # Đảm bảo BrowserSetup được định nghĩa đúng
        self.driver.maximize_window()  # Mở trình duyệt toàn màn hình
        self.driver.get("https://demoqa.com/text-box")

    def test_enter_data_successfully(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)  # Chờ tối đa 10s nếu phần tử chưa xuất hiện

        # Nhập FullName
        txtFullName = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        txtFullName.send_keys("Đinh Ngọc Thế Nhân")

        # Nhập Email
        txtEmail = driver.find_element(By.ID, "userEmail")
        txtEmail.send_keys("nhan105534@donga.edu.vn")

        # Nhập Địa chỉ hiện tại
        txtCurrentAddress = driver.find_element(By.ID, "currentAddress")
        txtCurrentAddress.send_keys("Nhà sáng tác Đà Nẵng")

        # Nhập Địa chỉ thường trú
        txtPermanentAddress = driver.find_element(By.ID, "permanentAddress")
        txtPermanentAddress.send_keys("Khu Phố 1 - Phường 1 - Thị xã Quảng Trị")

        # Nhấn Submit
        btnSubmit = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].click();", btnSubmit)  # Sử dụng JavaScript để tránh lỗi che khuất nút

        # Chờ dữ liệu hiển thị trong output
        time.sleep(10)  # Đợi một chút để tránh lỗi Selenium không lấy được dữ liệu

        # Kiểm tra kết quả hiển thị đúng không
        output = driver.find_element(By.ID, "output").text

        self.assertIn("Đinh Ngọc Thế Nhân", output, "Tên không đúng!")
        self.assertIn("nhan105534@donga.edu.vn", output, "Email không đúng!")
        self.assertIn("Nhà sáng tác Đà Nẵng", output, "Địa chỉ hiện tại không đúng!")
        self.assertIn("Khu Phố 1 - Phường 1 -Thị xã Quảng Trị", output, "Địa chỉ thường trú không đúng!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
