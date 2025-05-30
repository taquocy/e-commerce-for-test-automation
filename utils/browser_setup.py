import configparser
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Tạo options cho Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Chạy headless trong CI
        options.add_argument('--no-sandbox')  # Cần thiết cho CI
        options.add_argument('--disable-dev-shm-usage')  # Tránh lỗi bộ nhớ
        options.add_argument('--disable-gpu')  # Tắt GPU trong headless
        temp_dir = tempfile.mkdtemp()  # Tạo thư mục tạm duy nhất
        options.add_argument(f'--user-data-dir={temp_dir}')

        # Sử dụng webdriver_manager để tự động tải ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)
        return driver