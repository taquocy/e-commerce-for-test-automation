import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        # Tạo instance của WebDriver (Chrome ở đây) sử dụng Service
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)

        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver
