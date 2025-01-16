from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasketPage:
    def __init__(self, driver):
        self.driver = driver

        # Cập nhật lại các phần tử
        self.remove_button = (By.XPATH, "//*[@id='content']/div//button")  # Xóa sản phẩm khỏi giỏ
        self.basket_button = (By.XPATH, "//a[@href='/basket']")  # Mở giỏ hàng
        self.item_image = (By.XPATH, "//*[@id='content']/div//a/img")  # Ảnh sản phẩm trong giỏ
        self.total_price = (By.XPATH, "//p[contains(text(), 'Total:')]")  # Giá tổng cộng trong giỏ hàng
        self.item_in_basket = (By.XPATH, "//*[@id='content']/div//div[contains(@class, 'basket-item')]")  # Kiểm tra sản phẩm trong giỏ hàng

    def open_basket(self):
        self.driver.find_element(*self.basket_button).click()

    def remove_item_from_basket(self):
        self.driver.find_element(*self.remove_button).click()

    def get_item_image_src(self):
        return self.driver.find_element(*self.item_image).get_attribute("src")

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text

    def is_item_in_basket(self):
        try:
            # Kiểm tra sự tồn tại của ít nhất một sản phẩm trong giỏ hàng
            self.driver.find_element(*self.item_in_basket)
            return True  # Nếu phần tử được tìm thấy, trả về True
        except NoSuchElementException:
            return False  # Nếu không tìm thấy phần tử, trả về False
