import unittest
import configparser
import HtmlTestRunner
import sys
import os
from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.list_order import OrderPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Add root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ListOrderTest(unittest.TestCase):

    def setUp(self):
        # Load configuration from config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        # Get login URL from config
        self.login_url = config['app']['login_url']
        
        # Initialize the browser and open the login page
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)
        
        # Log in to the application
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()
    
    def test_list_order(self):
        # Navigate to the admin page
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        
        # Ensure the open_order_page method exists in AdminPage
        if hasattr(admin_page, 'open_order_page'):
            # Attempt to open the order page
            list_order = admin_page.open_order_page()
            
            # You can add additional checks or assertions here
            # For example, check if an order list element is present
            self.assertIsNotNone(list_order, "Order page did not load correctly")
        else:
            self.fail("AdminPage does not have a method named 'open_order_page'")
    
    def tearDown(self):
        # Quit the browser after each test
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
