from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasketPage:
    def __init__(self, driver):
        self.driver = driver

        # Các phần tử trên trang
        self.home_button = (By.XPATH, "//a[normalize-space(text())='eCommerce']")  # Nút về trang chủ
        self.add_button = (By.XPATH, "(//button[@class='chakra-button css-4nu9hl'])[2]")  # Nút thêm sản phẩm
        self.basket_button = (By.XPATH, "//button[@class='chakra-button css-19qgvsf']")  # Nút giỏ hàng
        self.remove_button = (By.XPATH, "//button[@class='chakra-button css-kwsp43']")  # Nút xóa sản phẩm

    def go_home(self):
        """Quay về trang chủ."""
        self.driver.find_element(*self.home_button).click()

    def add_to_basket(self):
        """Thêm sản phẩm vào giỏ hàng."""
        self.driver.find_element(*self.add_button).click()

    def open_basket(self):
        """Mở giỏ hàng."""
        self.driver.find_element(*self.basket_button).click()

    def remove_item(self):
        """Xóa sản phẩm khỏi giỏ hàng."""
        self.driver.find_element(*self.remove_button).click()

    def is_basket_button_displayed(self):
        """Kiểm tra xem nút giỏ hàng có hiển thị không."""
        try:
            basket_button = self.driver.find_element(*self.basket_button)
            return basket_button.is_displayed()
        except NoSuchElementException:
            return False
