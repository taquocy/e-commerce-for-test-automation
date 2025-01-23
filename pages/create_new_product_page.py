from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewProductPage():
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.title_label = (By.XPATH, "//label[@for='field-:r2:']")  # Label Title
        self.title_input = (By.NAME, "title")  # Trường input Title
        self.title_error = (By.XPATH, "//p[contains(text(), 'title is a required field')]")  # Thông báo lỗi Title

        self.description_label = (By.XPATH, "//label[@for='field-:r3:']")  # Label Description
        self.description_input = (By.XPATH, "//textarea[@name='description']")  # Textarea Description

        self.price_label = (By.XPATH, "//label[@for='field-:r4:']")  # Label Price
        self.price_input = (By.XPATH, "//input[@name='price']")  # Trường input Price

        self.photos_label = (By.XPATH, "//label[@for='field-:r5:']")  # Label Photos
        self.add_photo_button = (By.XPATH, "//button[text()='Add a Photo']")  # Nút "Add a Photo"
        self.photo_input = (By.XPATH, "//input[@name='photos.0']")

        self.add_product_button = (By.XPATH, "//button[@type='submit']")  # Nút "Add Product"
        self.message_create_product_successfully = (By.XPATH, "//span[text()='Add product successfully']")



    def enter_title(self, title):
        """Nhập Title. """
        self.driver.find_element(*self.title_input).send_keys(title)

    def enter_description(self, description):
        """Nhập Description ."""
        self.driver.find_element(*self.description_input).send_keys(description)

    def enter_price(self, price):
        """Nhập Price ."""
        self.driver.find_element(*self.price_input).send_keys(price)

    def click_add_photo(self):
        """Nhấn nút 'Add a Photo'."""
        self.driver.find_element(*self.add_photo_button).click()

    def enter_image_url(self, image):
        """Nhấn nút 'Add a Photo'."""
        self.driver.find_element(*self.photo_input).click()
        self.driver.find_element(*self.photo_input).send_keys(image)

    def click_add_product(self):
        """Nhấn nút 'Add Product' để đăngđăng."""
        self.driver.find_element(*self.add_product_button).click()

    def is_success_message_appeared(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.message_create_product_successfully)
            )
            print("Message 'Add product successfully' appeared!")
            return True
        except TimeoutException:
            print("Message 'Add product successfully' did not appear.")
            return False


