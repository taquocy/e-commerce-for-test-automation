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

        # Sử dụng Service để quản lý đường dẫn driver
        service = Service(driver_path)

        # Tạo instance của WebDriver (Chrome ở đây) với service
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(26)  # Thiết lập thời gian chờ implicit
        driver.maximize_window()    # Mở rộng cửa sổ trình duyệt
        return driver
