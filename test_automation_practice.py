import unittest
import configparser
import HtmlTestRunner
import sys
import os
from selenium.webdriver.common.by import By

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class ST23ATestCaseAuto(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/webtables")  # Sử dụng URL từ file config

    def test_enter_data_sucescssully(self):
        # Bước 1: Nhấn vào nút "Add"
        btnAdd = self.driver.find_element(By.XPATH, "//button[@id=\"addNewRecordButton\"]")
        btnAdd.click()
        # Bước 2: Nhập tên = 'Hoang'
        txtFirstName = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
        txtFirstName.send_keys("Hoang")
        # Bước 3: Nhập họ = 'Tran'
        txtLastName = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
        txtLastName.send_keys("Tran")
        # Bước 4: Nhập Email = 'hoang104094@donga.edu.vn'
        txtEmail = self.driver.find_element(By.ID, "userEmail")
        txtEmail.send_keys("hoang104094@donga.edu.vn")
        # Bước 5: Nhập Tuổi = '20'
        txtAge = self.driver.find_element(By.CSS_SELECTOR, "#age")
        txtAge.send_keys("20")
        # Bước 6: Nhập Lương = '20000000'
        txtSalary = self.driver.find_element(By.XPATH, "//input[@id='salary']")
        txtSalary.send_keys("20000000")
        # Bước 7: Nhập Phòng ban = 'IT'
        txtDepartMent = self.driver.find_element(By.XPATH, "//input[@id='department']")
        txtDepartMent.send_keys("IT")
        # Bước 8: Nhấn nút "Submit"
        self.driver.find_element(By.ID, "submit").click()
        # Bước 9: Kiểm tra dữ liệu xuất hiện trên bảng
        table = self.driver.find_element(By.XPATH, "//div[@class='rt-table']")
        assert "hoang104094@donga.edu.vn" in table.text, "Thêm dữ liệu thất bại!"
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
