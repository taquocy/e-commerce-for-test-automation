import unittest
import configparser
import HtmlTestRunner
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.home_page import HomePage 
from utils.browser_setup import BrowserSetup 

class HomePageTest(unittest.TestCase):

    def setUp(self):
    
        config = configparser.ConfigParser()
        config.read('config.ini')
    
        self.home_url = config['app']['login_url']

        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.home_url)  
    def test_product_details_display(self):
        home_page = HomePage(self.driver)

        product_title = home_page.get_product_title()
        product_time = home_page.get_product_time()
        product_price = home_page.get_product_price()

        self.assertTrue(product_title, "Product title is not displayed")
        self.assertTrue(product_time, "Product time is not displayed")
        self.assertTrue(product_price, "Product price is not displayed")

    def test_add_to_basket(self):
        home_page = HomePage(self.driver)
      
        home_page.click_add_to_basket()
       
    def test_add_to_cart(self):
        home_page = HomePage(self.driver)

        home_page.click_add_to_cart()
     
    def test_navigation_buttons(self):
        home_page = HomePage(self.driver)
 
        home_page.click_login()
      
        home_page.click_register()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
