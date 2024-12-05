from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.order_page import OrderProductPage

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_product =  (By.XPATH, "//a[@href='/']")

    def open_product_page(self):
        self.driver.find_element(*self.menu_product).click()
        return OrderProductPage(self.driver)



    def check_product_page_display(self):
        try:
            product_button = self.driver.find_element(By.XPATH, "//a[text()='Products']")

            assert product_button is not None, "Product button does not exist!"
            print("Product button exists!")

        except NoSuchElementException:
            print("Product button not found!")

