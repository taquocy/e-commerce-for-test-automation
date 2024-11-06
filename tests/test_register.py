import unittest
import configparser
import HtmlTestRunner
import sys
import os
from selenium.webdriver.common.by import By  # Make sure to import By here

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup


class RegisterTest(unittest.TestCase):


    

    def setUp(self):
        # Read the config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get the URL for the registration page
        self.register_url = config['app']['register_url']

        # Initialize the browser
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.register_url)  # Navigate to the registration page

    def test_valid_register_new_user(self):
        register_page = RegisterPage(self.driver)

        # Open registration form and fill in details
        register_page.open_register_form()
        register_page.enter_email("johndoe@email.com")
        register_page.enter_password("password123")
        register_page.enter_confirm_password("password123")
        register_page.click_register()

        # Add assertions to verify successful registration
        # Example: Check if a success message or redirection occurs.
        # Modify the XPath to match the actual success message element in your application
        success_message = self.driver.find_element(By.XPATH, "//div[@class='success-message']")
        self.assertTrue(success_message.is_displayed(), "Registration failed or success message not displayed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

