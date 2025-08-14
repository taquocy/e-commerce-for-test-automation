from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EditProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.title_input = (By.XPATH, "//input[@name='title']")
        self.description_input = (By.XPATH, "//textarea[@name='description']")
        self.price_input = (By.XPATH, "//input[@name='price']")
        self.photo_input = (By.XPATH, "//input[@name='photos.0']")
        self.add_product_button = (By.XPATH, "//button[@type='submit']")
        self.message_create_product_successfully = (By.XPATH, "//span[text()='The product successfully updates']")

    def enter_title(self, title):
        """Enter Title into the title field."""
        title_element = self.driver.find_element(*self.title_input)
        title_element.send_keys(Keys.COMMAND + "a")  # Select all text
        title_element.send_keys(Keys.BACKSPACE)  # Clear text
        title_element.send_keys(title)

    # def clear_title(self):
    #     """Nhập Title vào trường Title."""
    #     title_element = self.driver.find_element(*self.title_input)
    #     title_element.send_keys(Keys.COMMAND + "a")  # Chọn toàn bộ văn bản
    #     title_element.send_keys(title)

    def enter_description(self, description):
        """Enter Description into the description field."""
        description_element = self.driver.find_element(*self.description_input)
        description_element.send_keys(Keys.COMMAND + "a")
        description_element.send_keys(Keys.BACKSPACE)
        description_element.send_keys(description)

    def enter_price(self, price):
        """Enter Price into the price field."""
        price_element = self.driver.find_element(*self.price_input)
        price_element.send_keys(Keys.COMMAND + "a")
        price_element.send_keys(Keys.BACKSPACE)
        price_element.send_keys(price)

    def enter_image_url(self, image):
        """Upload image via the input field."""
        image_element = self.driver.find_element(*self.photo_input)
        image_element.send_keys(Keys.COMMAND + "a")
        image_element.send_keys(Keys.BACKSPACE)
        image_element.send_keys(image)

    def click_add_product(self):
        """Click 'Add Product' button to submit the form."""
        self.driver.find_element(*self.add_product_button).click()

    def is_success_message_appeared(self):
        """Check if the success message is displayed."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.message_create_product_successfully)
            )
            print("Message 'The product successfully updates' appeared!")
            return True
        except TimeoutException:
            print("Message 'The product successfully updates' did not appear.")
            # Optionally, take a screenshot for debugging
            self.driver.save_screenshot("error_screenshot.png")
            return False




