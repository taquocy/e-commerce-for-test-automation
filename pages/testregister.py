# Test register á
import unittest
import configparser
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.driver.get("https://demoqa.com/login")  # Sử dụng URL từ file config

    def test_add_new_data_succesfully(self):
       #Summary: Verify that the user can add new user accounts successfully
       #Step1 : Click on New User button
       btnUser = self.driver.find_element(By.XPATH,"//button[@id='newUser']")
       btnUser.click()
       time.sleep(1)

       #Step2: Enter FirstName = 'Yaly'
       txtFirstName= self.driver.find_element(By.XPATH,"//input[@id='firstname']")
       txtFirstName.send_keys("Yaly")
       time.sleep(1)

       #Step3: Enter LastName = 'Ho'
       txtLastName= self.driver.find_element(By.XPATH,"//input[@id='lastname']")
       txtLastName.send_keys("Ho")
       time.sleep(1)

       #Step4: Enter UserName = 'hoyaly123'
       txtUserName=self.driver.find_element(By.XPATH,"//input[@id='userName']")
       txtUserName.send_keys("hoyaly123")
       time.sleep(1)

       #Step5: Enter PassWord = 'ckneSeTQsLi4@y9'
       txtPass=self.driver.find_element(By.XPATH,"//input[@id='password']")
       txtPass.send_keys("ckneSeTQsLi4@y9")
       time.sleep(1)

       #Step6: Click on recaptcha
       iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
       self.driver.switch_to.frame(iframe)
       recaptcha_box = self.driver.find_element(By.ID, "recaptcha-anchor")
       ActionChains(self.driver).move_to_element(recaptcha_box).click().perform() 
       time.sleep(5)

       self.driver.switch_to.default_content()
       
       #Step7: Click on Register button
       btnRegis = WebDriverWait(self.driver, 10).until(
       EC.element_to_be_clickable((By.XPATH, "//button[@id='register']"))
       )
       btnRegis.click()
       time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
