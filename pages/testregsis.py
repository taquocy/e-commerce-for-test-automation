from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests 

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
        self.driver.get("https://demoqa.com/login")  # Sử dụng URL từ file config

    def test_add_new_data_succesfully(self):
       #Summary: Verify that the user can successfully register new users
       #Step1 : Click on Add button
    #    btnAdd = self.driver.find_element(By.XPATH,"//button[@id='newUser']")
    #    btnAdd.click()
    #    time.sleep(3)

    #    #Step2: Enter FirstName = 'Ly'
    #    txtFirstName= self.driver.find_element(By.XPATH,"//input[@id=\"firstname\"]")
    #    txtFirstName.send_keys("Ly")
    #    time.sleep(3)

    #    #Step3: Enter LastName = 'Ya'
    #    txtLastName= self.driver.find_element(By.XPATH,"//input[@id=\"lastname\"]")
    #    txtLastName.send_keys("Ya")
    #    time.sleep(3)

       #Step4: Enter Username = 'yaly248'
       txtUser=self.driver.find_element(By.XPATH,"//input[@id='userName']")
       txtUser.send_keys("Yaly248")
       time.sleep(3)

       #Step5: Enter Password = 'yaly248204'
       txtPassword=self.driver.find_element(By.XPATH,"//input[@id='password']")
       txtPassword.send_keys("ckneSeTQsLi4@y9")
       time.sleep(3)

    #    #Step7: Click box recaptcha
    #    iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    #    self.driver.switch_to.frame(iframe)
    #    recaptcha_box = self.driver.find_element(By.ID, "recaptcha-anchor")
    #    ActionChains(self.driver).move_to_element(recaptcha_box).click().perform()
    #    time.sleep(3)

    #    #Step8: Click on Submit button
    #    btnRegis=self.driver.find_element(By.XPATH,"//button[@id='register']")
    #    btnRegis.click()
    #    time.sleep(3)
           #Step8: Click on Submit button
       btnLogin=self.driver.find_element(By.XPATH,"//button[@id='login']")
       btnLogin.click()
       time.sleep(3)
       
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))