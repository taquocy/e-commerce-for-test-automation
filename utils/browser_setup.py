# import configparser
# from selenium import webdriver

# class BrowserSetup:
#     @staticmethod
#     def get_driver():
#         # Đọc file config.ini
#         config = configparser.ConfigParser()
#         config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

#         # Lấy path driver từ phần cấu hình webdriver
#         driver_path = config['webdriver']['driver_path']

#         # Tạo instance của WebDriver (Chrome ở đây)
#         driver = webdriver.Chrome(executable_path=driver_path)
#         driver.implicitly_wait(26)
#         driver.maximize_window()
#         return driver

import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
<<<<<<< HEAD

=======
>>>>>>> 5d0ff936489f1faa2aa2cecb29bd17b37b1e4d52

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

<<<<<<< HEAD
        # Tạo instance của WebDriver (Chrome ở đây)          
=======
>>>>>>> 5d0ff936489f1faa2aa2cecb29bd17b37b1e4d52
        service = Service(driver_path)  # Create a Service object with the path to chromedriver
        driver = webdriver.Chrome(service=service)

        # Tạo instance của WebDriver (Chrome ở đây)
        # driver = webdriver.Chrome(executable_path=driver_path)
        driver.implicitly_wait(26)
        driver.maximize_window()
<<<<<<< HEAD
        return driver

=======
        return driver
>>>>>>> 5d0ff936489f1faa2aa2cecb29bd17b37b1e4d52
