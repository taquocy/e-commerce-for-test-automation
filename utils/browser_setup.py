import configparser
from selenium import webdriver

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        # Tạo instance của WebDriver (Chrome ở đây)
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver
