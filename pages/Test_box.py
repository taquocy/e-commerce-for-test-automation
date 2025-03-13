import unittest
import configparser
import HtmlTestRunner
import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class NhiTest(unittest.TestCase):
    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/webtables")
        self.wait = WebDriverWait(self.driver, 10)

    def test_add_new_data_succesfully(self):
        # Click vào nút "Add"
        btnAdd = self.wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        btnAdd.click()

        # Nhập dữ liệu vào form
        txtFirstName = self.wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
        txtFirstName.send_keys("Le Thi Ngoc")

        txtLastName = self.driver.find_element(By.ID, "lastName")
        txtLastName.send_keys("Nhi")

        txtEmail = self.driver.find_element(By.ID, "userEmail")
        txtEmail.send_keys("nhi@donga.edu.vn")

        txtAge = self.driver.find_element(By.ID, "age")
        txtAge.send_keys("25")

        txtSalary = self.driver.find_element(By.ID, "salary")
        txtSalary.send_keys("5000")

        txtDepartment = self.driver.find_element(By.ID, "department")
        txtDepartment.send_keys("IT")

        # Click nút Submit
        btnSubmit = self.driver.find_element(By.ID, "submit")
        btnSubmit.click()

        # Kiểm tra dữ liệu đã nhập thành công
        table = self.driver.find_element(By.CLASS_NAME, "rt-table")
        assert "Le Thi Ngoc" in table.text
        assert "Nhi" in table.text
        assert "nhi@donga.edu.vn" in table.text

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
