from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.add_to_basket_button = (By.XPATH, "//button[text()='Add to Basket']")
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to Cart']")
        self.load_more_button = (By.XPATH, "//button[text()='Load More']")

    def click_add_to_basket(self):
        self.driver.find_element(*self.add_to_basket_button).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_load_more(self):
        self.driver.find_element(*self.load_more_button).click()

    def is_add_to_basket_button_displayed(self):
        try:
            return self.driver.find_element(*self.add_to_basket_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_add_to_cart_button_displayed(self):
        try:
            return self.driver.find_element(*self.add_to_cart_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_load_more_button_displayed(self):
        try:
            return self.driver.find_element(*self.load_more_button).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_load_more_results(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='new-content-loaded']"))
            )
            print("New content loaded successfully!")
            return True
        except TimeoutException:
            print("New content did not load.")
            return False