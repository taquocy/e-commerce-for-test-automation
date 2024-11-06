import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Load configuration file
        config = configparser.ConfigParser()
        config.read('path_to_your_config.ini')  # Path to your config file

        # Get the driver path from the configuration
        driver_path = config['webdriver']['driver_path']

        # Create a Service object with the driver path
        service = Service(driver_path)

        # Initialize the Chrome driver with the service
        driver = webdriver.Chrome(service=service)
        return driver
