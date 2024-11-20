import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Thêm dòng này để import lớp Service

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy đường dẫn đến driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        # Khởi tạo đối tượng Service với đường dẫn ChromeDriver
        service = Service(driver_path)  

        # Tạo instance của WebDriver (Chrome ở đây)
        driver = webdriver.Chrome(service=service)

        # Cài đặt thời gian chờ ngầm định và phóng to cửa sổ
        driver.implicitly_wait(26)
        driver.maximize_window()

        return driver
