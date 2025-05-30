from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CreateNewProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_input = (By.CSS_SELECTOR, "input[name='title']")
        self.description_input = (By.CSS_SELECTOR, "textarea[name='description']")
        self.price_input = (By.CSS_SELECTOR, "input[name='price']")
        self.add_photo_button = (By.CSS_SELECTOR, "button.chakra-button.css-196gjj0")
        self.photo_input = (By.CSS_SELECTOR, "input[name^='photos.0']")
        self.add_product_button = (By.CSS_SELECTOR, "button[type='submit'].chakra-button.css-1qqymvj")
        self.message_create_product_successfully = (By.XPATH, "//span[contains(text(), 'Add Product is successfully')]")

    def enter_title(self, title):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.title_input)
            )
            elem.click()
            elem.clear()
            elem.send_keys(title)
            logging.info(f"Entered title: {title}")
        except TimeoutException:
            logging.error("❌ Timeout waiting for title input")
            raise

    def enter_description(self, description):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.description_input)
            )
            elem.click()
            elem.clear()
            elem.send_keys(description)
            logging.info(f"Entered description: {description}")
        except TimeoutException:
            logging.error("❌ Timeout waiting for description input")
            raise

    def enter_price(self, price):
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.price_input)
            )
            elem.click()
            elem.clear()
            elem.send_keys(price)
            logging.info(f"Entered price: {price}")
        except TimeoutException:
            logging.error("❌ Timeout waiting for price input")
            raise

    def click_add_photo(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_photo_button)
            ).click()
            time.sleep(1)
            logging.info("Clicked Add a Photo button")
        except TimeoutException:
            logging.error("❌ Timeout waiting for Add a Photo button")
            raise

    def enter_image_url(self, image):
    
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.photo_input)
            )
            elem.click()
            elem.clear()
            elem.send_keys(image)
            logging.info(f"Entered image URL: {image}")
        except TimeoutException:
            logging.error("❌ Timeout waiting for photo input")
            raise

    def click_add_product(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_product_button)
            ).click()
            logging.info("Clicked Add Product button")
        except TimeoutException:
            logging.error("❌ Timeout waiting for Add Product button")
            raise

    def is_success_message_appeared(self):
        try:
            WebDriverWait(self.driver, 15).until(  # Tăng timeout
                EC.visibility_of_element_located(self.message_create_product_successfully)
            )
            logging.info("✅ Success message 'Add product successfully' appeared")
            return True
        except TimeoutException:
            logging.error("❌ Success message did not appear")
            return False