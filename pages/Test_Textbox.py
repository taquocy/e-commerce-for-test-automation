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

class NhiTest(unittest.TestCase):
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
        #Step1 : Click on Add button
        btnAdd = self.driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']")
        btnAdd.click()
        #Step1: Enter FullName = 'Le Thi Ngoc Nhi'
        txtFullName= self.driver.find_element(By.XPATH,"//input[@id=\"fullName\"]")
        txtFullName.send_keys("Le Thi Ngoc Nhi")

        #step2: Enter Email = "nhi@donga.edu.vn"
        txtEmail= self.driver.find_element(By.XPATH,"//input[@id=\"Email\"]")
        txtEmail.send_keys("nhi@donga.edu.vn")
        #step3: Enter CurrentAddress = "Xo Viet Nghe Tinh, Hai Chau, DN"
        txtCurrentAddress= self.driver.find_element(By.XPATH,"//input[@id=\"currentAddress\"]")
        txtCurrentAddress.send_keys("Xo Viet Nghe Tinh, Hai Chau, DN")
        #step4: Enter PermanentAddress = "Nguyen Tri Phuong, Hai Chau, DN"
        txtPermanentAddress= self.driver.find_element(By.XPATH,"//input[@id=\"permanentAddress\"]")
        txtPermanentAddress.send_keys("Nguyen Tri Phuong, Hai Chau, DN")
        #step5: Click on Submit button
        btnSubmit= self.driver.find_element(By.XPATH,"//button[@id=\"submit\"]")
        btnSubmit.click()
        #Step6: Verify success message = "Form submitted successfully!"
        successMessage= self.driver.find_element(By.XPATH,"//p[@class=\"success-message\"]")
        self.assertEqual("Form submitted successfully!", successMessage.text)
        #step7: verify that new data is added successfully
        table = self.driver.find_element(By.XPATH,"//table[@id=\"rt-table\"]")
        assert "Le Thi Ngoc Nhi" in table.text
        assert "nhi@donga.edu.vn" in table.text
    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
