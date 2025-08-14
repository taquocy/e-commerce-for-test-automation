import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.browser_setup import BrowserSetup
import time

class WebTablePage(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/selectable")  # Sử dụng URL từ file config

    def test_selectable(self):
        time.sleep(5)

        click_list = self.driver.find_element(By.XPATH,"//*[@id='demo-tab-list']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", click_list)
        click_list.click()

        list_1 = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/ul/li[1]")
        list_1.click()

        list_2 = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/ul/li[3]")
        list_2.click()

        click_grid = self.driver.find_element(By.XPATH,"//*[@id='demo-tab-grid']")
        click_grid.click()

        grid_4 = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/li[1]")
        grid_4.click()

        grid_9 = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/li[3]")
        grid_9.click()

        grid_2 = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/li[2]")
        grid_2.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))