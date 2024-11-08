class BasketPage():
    def __init__(self, driver):
        self.driver = driver

        # Các phần tử liên quan đến giỏ hàng
        self.product_name_input = (By.NAME, "product_name")  # Trường nhập tên sản phẩm
        self.product_quantity_input = (By.NAME, "quantity")  # Trường nhập số lượng sản phẩm
        self.add_to_basket_button = (By.XPATH, "//button[text()='Add to Basket']")  # Nút thêm sản phẩm vào giỏ
        self.view_basket_button = (By.XPATH, "//a[text()='View Basket']")  # Nút xem giỏ hàng
        self.basket_item_list = (By.XPATH, "//div[@class='basket-items']")  # Danh sách các sản phẩm trong giỏ
        self.checkout_button = (By.XPATH, "//button[text()='Checkout']")  # Nút thanh toán

    def enter_product_name(self, product_name):
        """Nhập tên sản phẩm vào trường nhập tên sản phẩm."""
        self.driver.find_element(*self.product_name_input).send_keys(product_name)

    def enter_product_quantity(self, quantity):
        """Nhập số lượng sản phẩm vào trường nhập số lượng."""
        self.driver.find_element(*self.product_quantity_input).send_keys(quantity)

    def click_add_to_basket(self):
        """Nhấn nút 'Add to Basket' để thêm sản phẩm vào giỏ."""
        self.driver.find_element(*self.add_to_basket_button).click()

    def click_view_basket(self):
        """Nhấn nút 'View Basket' để xem giỏ hàng."""
        self.driver.find_element(*self.view_basket_button).click()

    def get_basket_items(self):
        """Lấy danh sách các sản phẩm trong giỏ hàng."""
        items = self.driver.find_elements(*self.basket_item_list)
        return [item.text for item in items]

    def click_checkout(self):
        """Nhấn nút 'Checkout' để thanh toán."""
        self.driver.find_element(*self.checkout_button).click()
