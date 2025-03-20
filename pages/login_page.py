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


class GD22BTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/webtables")  # Sử dụng URL từ file config

    def test_add_new_data_succesfully(self):
       #Summary: Verify that user can add new data successfully
       #Step1 : Click on  button
       btnEdit = self.driver.find_element(By.XPATH,"//button[@id='editRecordButton']")
       btnEdit.click()
       time.sleep(3)

       #Step2: Enter FirstName = 'Dao'
       txtFirstName= self.driver.find_element(By.XPATH,"//input[@id=\"Firstname\"]")
       txtFirstName.send_keys("Dao")
       time.sleep(3)

       #Step3: Enter LastName = 'Dieu'
       txtLastName= self.driver.find_element(By.XPATH,"//input[@id=\"Lastname\"]")
       txtLastName.send_keys("Dieu")
       time.sleep(3)

       #Step4: Enter Email = 'dieu99717@donga.edu.vn'
       txtEmail=self.driver.find_element(By.XPATH,"//input[@id=\"userEmail\"]")
       txtEmail.send_keys("dieu99717@donga.edu.vn")
       time.sleep(3)

       #Step5: Enter Age = '21'
       txtAge=self.driver.find_element(By.XPATH,"//input[@id=\"age\"]")
       txtAge.send_keys("21")
       time.sleep(3)


       #Step6: Enter Salary = '200000000'
       txtSalary=self.driver.find_element(By.XPATH,"//input[@id=\"salary\"]")
       txtSalary.send_keys("200000000")
       time.sleep(3)

       #Step7: Enter Department = 'Graphic Design'
       txtDepartment=self.driver.find_element(By.XPATH,"//input[@id=\"department\"]")
       txtDepartment.send_keys("Graphic Design")
       time.sleep(3)

       #Step8: Click on Submit button
       btnSubmit=self.driver.find_element(By.XPATH,"//button[@id=\"submit\"]")
       btnSubmit.click()
       time.sleep(3)

       #Step9: Verify that new data is added successfully
       table = self.driver.find_element(By.XPATH,"//div[@class=\"rt-table\"]")
       assert "khue99234@donga.edu.vn" in table.text
       assert "Graphic Design" in table.text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))