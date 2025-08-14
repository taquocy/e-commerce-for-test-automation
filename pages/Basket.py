from selenium.webdriver.common.by import By

class BasketPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên giỏ hàng
        self.product_name = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[1]/h2')]")  # Tên sản phẩm
        self.product_price = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[1]/p[2]")  # Giá sản phẩm
        self.remove_from_basket_button = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[2]/button")  # Nút xóa sản phẩm khỏi giỏ

    # Hàm để lấy tên sản phẩm trong giỏ hàng
    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text
    
    # Hàm để lấy giá sản phẩm trong giỏ hàng
    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    # Hàm để nhấn nút "Remove from basket" để xóa sản phẩm khỏi giỏ
    def click_remove_from_basket(self):
        self.driver.find_element(*self.remove_from_basket_button).click()
