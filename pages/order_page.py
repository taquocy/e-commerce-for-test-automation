from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderProductPage():
    def __init__(self, driver):
        self.driver = driver

        self.addToBasket_button = (By.CSS_SELECTOR, ".chakra-button.css-4nu9hl:first-of-type")  
        self.buyNow_button = (By.CSS_SELECTOR, ".chakra-button.css-1qs1wp9")  
        self.button_basket =  (By.XPATH, "//a[@href='/basket']/button")
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
    def add_basket(self):
        self.driver.find_element(*self.addToBasket_button).click()
    def open_basket_page(self):
        self.driver.find_element(*self.button_basket).click()
    def open_model_address(self):
        self.driver.find_element(*self.buyNow_button).click()

        # Xác định các phần tử trên trang login
        self.title_label = (By.XPATH, "//label[@for='field-:rf:']") 
        self.address_input = (By.XPATH, "//textarea[contains(@class, 'chakra-textarea') and contains(@class, 'css-1msuebi')]")
        self.save_address = (By.XPATH, "//button[contains(@class, 'chakra-button') and contains(@class, 'css-f2hjvb')]")


    def enter_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def click_save(self):
        self.driver.find_element(*self.save_address).click()


