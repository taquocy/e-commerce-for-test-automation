from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasketPage:
    def __init__(self, driver):
        self.driver = driver

        self.remove_button = (By.XPATH, "//*[@id='content']/div//button")
        self.basket_button = (
            By.XPATH, "//*[@id='root']/nav/div[2]/a[@href='/basket']")
        self.item_image = (By.XPATH, "//*[@id='content']/div//a/img")
        self.total_price = (By.XPATH, "//p[contains(text(), 'Total:')]")
        
    def open_basket(self):
        self.driver.find_element(*self.basket_button).click()

    def remove_item_from_basket(self):
        
        self.driver.find_element(*self.remove_button).click()


    def get_item_image_src(self):
        return self.driver.find_element(*self.item_image).get_attribute("src")

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text
