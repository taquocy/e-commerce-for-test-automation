from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import configparser
import HtmlTestRunner
import sys
import os
from selenium.webdriver.common.by import By

# Add root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.basket_page import BasketPage  # If still needed
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.browser_setup import BrowserSetup


class BasketButtonTest(unittest.TestCase):

    def setUp(self):
        # Read config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get login and home URLs from config
        self.login_url = config['app']['login_url']
        self.home_url = config['app']['home_url']

        # Initialize browser
        self.driver = BrowserSetup.get_driver()
        
        # Open login page and perform login
        self.driver.get(self.login_url)
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

    def test_add_item_and_check_basket_button(self):
        # Navigate to home page after login
        self.driver.get(self.home_url)
        home_page = HomePage(self.driver)

        # Add an item to the basket from the home page
        home_page.add_item_to_basket()

        # Wait for the basket button to update with the item
        wait = WebDriverWait(self.driver, 10)
        
        # Locator for the basket icon with a badge or item count (Update based on actual UI)
        basket_button = (By.XPATH, "//*[@id='root']/nav/div[2]/a[1]/button")
        basket_item_indicator = wait.until(EC.presence_of_element_located(basket_button))
        
        # Verify item presence by checking badge, count, or visual update in the basket button
        basket_text = basket_item_indicator.text  # Adjust if there's a count or badge
        
        self.assertTrue(basket_text, "The basket button should indicate an item was added.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
