from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewProductPage():
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.title_label = (By.XPATH, "//label[@for='field-:r2:']")  # Label cho Title
        self.title_input = (By.NAME, "title")  # Trường input cho Title
        self.title_error = (By.XPATH, "//p[contains(text(), 'title is a required field')]")  # Thông báo lỗi cho Title

        self.description_label = (By.XPATH, "//label[@for='field-:r3:']")  # Label cho Description
        self.description_input = (By.XPATH, "//textarea[@name='description']")  # Textarea cho Description

        self.price_label = (By.XPATH, "//label[@for='field-:r4:']")  # Label cho Price
        self.price_input = (By.XPATH, "//input[@name='price']")  # Trường input cho Price

        self.photos_label = (By.XPATH, "//label[@for='field-:r5:']")  # Label cho Photos
        self.add_photo_button = (By.XPATH, "//button[text()='Add a Photo']")  # Nút "Add a Photo"
        self.photo_input = (By.XPATH, "//input[@name='photos.0']")

        self.add_product_button = (By.XPATH, "//button[@type='submit']")  # Nút "Add Product"
        self.message_create_product_successfully = (By.XPATH, "//span[text()='Add product successfully']")



    def enter_title(self, title):
        """Nhập Title vào trường Title."""
        self.driver.find_element(*self.title_input).send_keys(title)

    def enter_description(self, description):
        """Nhập Description vào trường Description."""
        self.driver.find_element(*self.description_input).send_keys(description)

    def enter_price(self, price):
        """Nhập Price vào trường Price."""
        self.driver.find_element(*self.price_input).send_keys(price)

    def click_add_photo(self):
        """Nhấn nút 'Add a Photo'."""
        self.driver.find_element(*self.add_photo_button).click()

    def enter_image_url(self, image):
        """Nhấn nút 'Add a Photo'."""
        self.driver.find_element(*self.photo_input).click()
        self.driver.find_element(*self.photo_input).send_keys(image)

    def click_add_product(self):
        """Nhấn nút 'Add Product' để gửi form."""
        self.driver.find_element(*self.add_product_button).click()

    def is_success_message_appeared(self):
        try:
            # Chờ đợi tối đa 10 giây cho thông báo "Add product successfully" xuất hiện
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.message_create_product_successfully)
            )
            print("Message 'Add product successfully' appeared!")
            return True
        except TimeoutException:
            print("Message 'Add product successfully' did not appear.")
            return False


