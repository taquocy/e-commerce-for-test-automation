from selenium.webdriver.common.by import By

class ProductDetailtPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang e-commerce
        self.product_image = (By.XPATH, "//*[@id='content']/div/div/div[1]/div/div/div/div/img")  # Đường dẫn đến ảnh sản phẩm
        self.product_name = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[1]/h2")  # Tên sản phẩm
        self.product_description = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[1]/p[1]")  # Mô tả sản phẩm
        self.product_price = (By.XPATH, "//*[@id='content']/div/div/div[2]/div[1]/p[2]")  # Giá sản phẩm
        self.login_button = (By.XPATH, "//*[@id='root']/nav/div[2]/a[1]/button)")  # Nút đăng nhập
        self.register_button = (By.XPATH, "//*[@id='root']/nav/div[2]/a[2]/button)" ) # Nút đăng ký

    # Hàm để nhấn vào nút đăng nhập
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    # Hàm để nhấn vào nút đăng ký
    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    # Hàm để lấy tên sản phẩm
    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    # Hàm để lấy mô tả sản phẩm
    def get_product_description(self):
        return self.driver.find_element(*self.product_description).text

    # Hàm để lấy giá sản phẩm
    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text
