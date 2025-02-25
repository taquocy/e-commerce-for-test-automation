from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang Home
        self.add_to_basket_button = (By.XPATH, "//button[text() = 'Add to Basket']")
        self.add_to_cart_button = (By.XPATH, "//button[text() = 'Add to cart']")
        self.load_more_button = (By.XPATH, "//button[text() = 'Load More']")