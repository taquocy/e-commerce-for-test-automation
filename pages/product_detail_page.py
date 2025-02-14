from selenium.webdriver.common.by import By

class ProductDetailtPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang e-commerce
        self.product_image = (By.XPATH, "//img[@class='image-gallery-image']")  # Đường dẫn đến ảnh sản phẩm
        self.product_name = (By.XPATH, "//h2[@class='chakra-heading']")  # Tên sản phẩm
        self.product_description = (By.XPATH, "//div[@class='chakra-card__body']/p[1]")  # Mô tả sản phẩm
        self.product_price = (By.XPATH, "//div[@class='chakra-card__body']/p[2]")  # Giá sản phẩm
        self.login_button = (By.XPATH, "//a[@href='/signin']/button[@class='chakra-button']")  # Nút đăng nhập
        self.register_button = (By.XPATH, "//a[@href='/signup']/button[@class='chakra-button']" ) # Nút đăng ký
        self.add_to_bag_button = (By.XPATH, "//div[@class='chakra-card__footer']/button" ) # Nút thêm giỏ hàng

    # Hàm để nhấn vào nút đăng nhập
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    # Hàm để nhấn vào nút đăng ký
    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    # Hàm để nhấn vào nút thêm giỏ hàng
    def click_add_to_bag_button(self):
        self.driver.find_element(*self.add_to_bag_button).click()

    # Hàm để lấy tên sản phẩm
    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    # Hàm để lấy mô tả sản phẩm
    def get_product_description(self):
        return self.driver.find_element(*self.product_description).text

    # Hàm để lấy giá sản phẩm
    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text