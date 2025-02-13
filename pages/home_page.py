from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang Home
        self.add_to_basket_button = (By.XPATH, "//button[text()='Add to Basket']")
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to Cart']")
        self.load_more_button = (By.XPATH, "//button[text()='Load More']")

    def click_add_to_basket(self):
        """Nhấn nút 'Add to Basket'."""
        self.driver.find_element(*self.add_to_basket_button).click()

    def click_add_to_cart(self):
        """Nhấn nút 'Add to Cart'."""
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_load_more(self):
        """Nhấn nút 'Load More'."""
        self.driver.find_element(*self.load_more_button).click()

    def is_add_to_basket_button_displayed(self):
        """Kiểm tra xem nút 'Add to Basket' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.add_to_basket_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_add_to_cart_button_displayed(self):
        """Kiểm tra xem nút 'Add to Cart' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.add_to_cart_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_load_more_button_displayed(self):
        """Kiểm tra xem nút 'Load More' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.load_more_button).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_load_more_results(self):
        """Chờ cho nội dung mới xuất hiện sau khi nhấn 'Load More'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='new-content-loaded']"))
            )
            print("New content loaded successfully!")
            return True
        except TimeoutException:
            print("New content did not load.")
            return False
