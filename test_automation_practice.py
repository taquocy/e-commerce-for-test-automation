import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

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
        #Step1 : Tap on Add button
        btnAdd = self.driver.find_element(By.XPATH, "//button[@id=\"addNewRecordButton\"]")
        btnAdd.click()
        #Step2 : Enter firstname = 'Hoang'
        txtFirstName = self.driver.find_element(By.XPATH,"//input[@id='firstName']")
        txtFirstName.send_keys("Hoang")
        #Step3 : Enter lastname = 'Tran'
        txtLastName = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
        txtLastName.send_keys("Tran")
        #Step4 : Enter Email = 'hoang104094@donga.edu.vn'
        txtEmail = self.driver.find_element(By.ID, "userEmail")
        txtEmail.send_keys("hoang104094@donga.edu.vn")
        #step5: Enter Age = '20'
        txtAge = self.driver.find_element(By.CSS_SELECTOR, "#age")
        txtAge.send_keys("20")
        #step6: Enter Salary = '20000000'
        txtSalary = self.driver.find_element(By.XPATH, "//input[@id='salary']")
        txtSalary.send_keys("20000000")
        #Step 7: Enter Department = 'IT'
        txtDepartMent = self.driver.find_element(By.XPATH, "//input[@id='department']")
        txtDepartMent.send_keys("IT")
        #Step 8: Enter submit button
        self.driver.find_element(By.ID,"submit").click()
        #Step 9 : Check data appear on table
        table = self.driver.find_element(By.XPATH, "//div[@class='rt-table']")
        assert "hoang104094@donga.edu.vn" in table.text, "Thêm dữ liệu thất bại!"
        return True


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
