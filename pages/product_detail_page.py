from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang chi tiết sản phẩm
        self.product_image = (By.XPATH, "//img[@class='image-gallery-image']")
        self.product_name = (By.XPATH, "//h2[contains(@class, 'chakra-heading')]")
        self.product_description = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[1]")
        self.product_price = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[2]")
        self.login_button = (By.XPATH, "//a[@href='/signin']/button[contains(@class, 'chakra-button')]")
        self.register_button = (By.XPATH, "//a[@href='/signup']/button[contains(@class, 'chakra-button')]")
        self.add_to_bag_button = (By.XPATH, "//div[contains(@class, 'chakra-card__footer')]/button")
        self.remove_from_basket_button = (By.XPATH, "//div[contains(@class, 'chakra-card__footer')]/button[contains(text(), 'Remove from basket')]")

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def click_add_to_bag_button(self):
        self.driver.find_element(*self.add_to_bag_button).click()

    def click_remove_from_basket_button(self):
        self.driver.find_element(*self.remove_from_basket_button).click()

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    def get_product_description(self):
        return self.driver.find_element(*self.product_description).text

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def is_remove_from_basket_displayed(self):
        """Kiểm tra nút Remove from basket đã hiển thị chưa (tức là đã toggle)."""
        try:
            button = self.driver.find_element(*self.remove_from_basket_button)
            return button.is_displayed()
        except Exception:
            return False