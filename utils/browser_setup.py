import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        # Tạo instance của WebDriver (Chrome ở đây)
        service = Service(executable_path=driver_path)
        options = Options()
        # driver = webdriver.Chrome(service=service, options=options)
        # Cách mới để khởi tạo driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver
