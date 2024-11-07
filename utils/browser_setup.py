import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserSetup:
    @staticmethod
    def get_driver():

        config = configparser.ConfigParser()
        config.read('config.ini')

        driver_path = config['webdriver']['driver_path']
        service = Service(driver_path)

        options = webdriver.ChromeOptions()

        options.binary_location = config['chromium']['binary_location']

        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver

