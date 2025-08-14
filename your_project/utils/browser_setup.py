from selenium import webdriver

class BrowserSetup:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Mở rộng màn hình
        driver = webdriver.Chrome(options=options)
        return driver
