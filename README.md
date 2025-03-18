# e-commerce-for-test-automation
e-commerce for test automation

## DOWNLOAD
# Versions: https://googlechromelabs.github.io/chrome-for-testing/
# ChromeDriver on Window 129: https://www.chromedriverdownload.com/en/downloads/chromedriver-129-download


## INSTALL:
pip install selenium html-testRunner



## RUN TEST:
python -m unittest discover -s tests
python -m unittest tests.test_login
python -m unittest tests.test_admin_new_product

python tests/run_tests.py



### FILE FOR WINDOW
## browser_setup.py
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        service = Service(driver_path)  # Create a Service object with the path to chromedriver
        driver = webdriver.Chrome(service=service)

        # Tạo instance của WebDriver (Chrome ở đây)
        # driver = webdriver.Chrome(executable_path=driver_path)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver

