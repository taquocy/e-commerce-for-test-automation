import unittest
import configparser

import HtmlTestRunner
import sys
import os
import time

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class ST23BTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/webtables")  # Sử dụng URL từ file config

    def test_can_add_valid_data_to_table(self):
        #Step1: Click on Add button to open Form
        btnAdd = self.driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']")
        btnAdd.click()
        time.sleep(2)

        #Step2: Enter FirstName = 'ST'
        txtFirstName = self.driver.find_element(By.XPATH,"//input[@id=\"firstName\"]")
        txtFirstName.send_keys("ST")
        time.sleep(2)

        #Step3: Enter LastName = '23B-CNTT'
        txtLastName = self.driver.find_element(By.XPATH,"//*[@id='lastName']")
        txtLastName.send_keys('23B-CNTT')
        time.sleep(2)

        #Step4: Enter Email = 'st23b@donga.edu.vn'
        txtEmail = self.driver.find_element(By.XPATH,"//*[@id='userEmail']")
        txtEmail.send_keys('st23b@donga.edu.vn')
        time.sleep(2)


        #Step5: Enter Age = '23'
        txtAge = self.driver.find_element(By.XPATH,"//*[@id='age']")
        txtAge.send_keys('23')
        time.sleep(2)

        #Step6: Enter Salary = '8000000'
        txtSalary = self.driver.find_element(By.XPATH,"//*[@id='salary']")
        txtSalary.send_keys('8000000')
        time.sleep(2)

        #Step7: Enter Department = 'CNTT'
        txtDepartment = self.driver.find_element(By.XPATH,"//input[@id=\"department\"]")
        txtDepartment.send_keys('CNTT')
        time.sleep(2)


        #Step8: Tap on Submit button
        btnSubmit = self.driver.find_element(By.XPATH, "//*[@id='submit']")
        btnSubmit.click()
        time.sleep(2)

        #Step9: Verify the data is added to the table
        table = self.driver.find_element(By.CSS_SELECTOR,".rt-table")
        assert "st23b@donga.edu.vn" in table.text




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

