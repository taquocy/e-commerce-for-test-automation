import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Gán đường dẫn trực tiếp cho driver
        driver_path = '/home/minhhau/Downloads/chromedriver-linux64(1)/chromedriver-linux64/chromedriver'

        # Khởi tạo Service cho ChromeDriver
        service = Service(driver_path)

        # Tạo instance của WebDriver (Chrome ở đây)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver
