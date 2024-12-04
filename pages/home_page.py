from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang Home
        self.add_to_basket_button = (By.XPATH, "//button[contains(text(),'Add to Basket')]")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(),'Add to Cart')]")
        self.load_more_button = (By.XPATH, "//button[contains(text(),'Load More')]")

    def click_add_to_basket(self):
        """Nhấn nút 'Add to Basket'."""
        try:
            self.driver.find_element(*self.add_to_basket_button).click()
        except NoSuchElementException:
            print("Error: 'Add to Basket' button not found.")

    def click_add_to_cart(self):
        """Nhấn nút 'Add to Cart'."""
        try:
            self.driver.find_element(*self.add_to_cart_button).click()
        except NoSuchElementException:
            print("Error: 'Add to Cart' button not found.")

    def click_load_more(self):
        """Nhấn nút 'Load More'."""
        try:
            self.driver.find_element(*self.load_more_button).click()
        except NoSuchElementException:
            print("Error: 'Load More' button not found.")

    def is_add_to_basket_button_displayed(self):
        """Kiểm tra xem nút 'Add to Basket' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.add_to_basket_button).is_displayed()
        except NoSuchElementException:
            print("Error: 'Add to Basket' button not displayed.")
            return False

    def is_add_to_cart_button_displayed(self):
        """Kiểm tra xem nút 'Add to Cart' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.add_to_cart_button).is_displayed()
        except NoSuchElementException:
            print("Error: 'Add to Cart' button not displayed.")
            return False

    def is_load_more_button_displayed(self):
        """Kiểm tra xem nút 'Load More' có xuất hiện trên trang không."""
        try:
            return self.driver.find_element(*self.load_more_button).is_displayed()
        except NoSuchElementException:
            print("Error: 'Load More' button not displayed.")
            return False

    def wait_for_load_more_results(self):
        """Chờ cho nội dung mới xuất hiện sau khi nhấn 'Load More'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'new-content-loaded')]"))
            )
            print("New content loaded successfully!")
            return True
        except TimeoutException:
            print("Error: New content did not load within the timeout.")
            return False

    def scroll_to_element(self, locator):
        """Cuộn trang để hiển thị một phần tử nếu nó không nằm trong khung nhìn."""
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            print(f"Scrolled to element: {locator}")
        except NoSuchElementException:
            print(f"Error: Element {locator} not found for scrolling.")
