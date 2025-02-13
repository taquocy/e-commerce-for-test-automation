import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

class BrowserSetup:
    @staticmethod
    def get_driver():
        try:
            # Đọc file config.ini
            config = configparser.ConfigParser()
            config_path = 'config.ini'  # Đường dẫn tới file config.ini
            if not os.path.exists(config_path):
                raise FileNotFoundError(f"File config.ini không tồn tại tại đường dẫn: {config_path}")
            
            config.read(config_path)

            # Lấy path driver từ phần cấu hình webdriver
            if 'webdriver' not in config or 'driver_path' not in config['webdriver']:
                raise KeyError("Cấu hình 'webdriver' hoặc khóa 'driver_path' không tồn tại trong file config.ini")

            driver_path = config['webdriver']['driver_path']

            # Kiểm tra xem file driver có tồn tại hay không
            if not os.path.exists(driver_path):
                raise FileNotFoundError(f"Driver không tồn tại tại đường dẫn: {driver_path}")

            # Tạo instance của WebDriver (Chrome ở đây)
            service = Service(driver_path)  # Tạo đối tượng Service với đường dẫn tới chromedriver
            driver = webdriver.Chrome(service=service)

            # Cấu hình mặc định cho trình duyệt
            driver.implicitly_wait(26)  # Đợi ngầm định
            driver.maximize_window()    # Mở cửa sổ trình duyệt tối đa
            return driver
        
        except FileNotFoundError as e:
            print(f"Lỗi: {e}")
        except KeyError as e:
            print(f"Lỗi: {e}")
        except WebDriverException as e:
            print(f"Lỗi khởi tạo WebDriver: {e}")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

    @staticmethod
    def get_urls():
        try:
            # Đọc file config.ini
            config = configparser.ConfigParser()
            config_path = 'config.ini'  # Đường dẫn tới file config.ini
            if not os.path.exists(config_path):
                raise FileNotFoundError(f"File config.ini không tồn tại tại đường dẫn: {config_path}")
            
            config.read(config_path)

            # Lấy các URL từ phần cấu hình app
            if 'app' not in config or 'login_url' not in config['app'] or 'home_url' not in config['app']:
                raise KeyError("Cấu hình 'app' hoặc các khóa 'login_url', 'home_url' không tồn tại trong file config.ini")

            login_url = config['app']['login_url']
            home_url = config['app']['home_url']

            return login_url, home_url
        
        except FileNotFoundError as e:
            print(f"Lỗi: {e}")
        except KeyError as e:
            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
