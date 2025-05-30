from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_basket_button = (By.CSS_SELECTOR, "button.chakra-button.css-4nu9hl")
        self.add_to_cart_button = (By.CSS_SELECTOR, "button.chakra-button.css-1tduvxh")
        self.load_more_button = (By.XPATH, "//button[text()='Load More']")
        self.product_title = (By.CSS_SELECTOR, "h2.chakra-heading.css-18j379d")
        self.product_time = (By.CSS_SELECTOR, "p.chakra-text.css-0")
        self.product_price = (By.CSS_SELECTOR, "p.chakra-text.css-3kjfdm")
        self.basket_count = (By.CSS_SELECTOR, "button.chakra-button.css-19qgvsf")
        self.cart_count = (By.CSS_SELECTOR, "button.chakra-button.css-1ut02yo")
        self.login_link = (By.XPATH, "//a[contains(@href, '/signin')]")
        self.register_link = (By.XPATH, "//a[contains(@href, '/signup')]")
        self.home_link = (By.XPATH, "//a[contains(text(), 'Products')]")
        self.profile_link = (By.CSS_SELECTOR, "button.chakra-button.css-ez23ye")  # Thêm Profile

    def click_add_to_basket(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_to_basket_button)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Add to Basket button")
            raise

    def click_add_to_cart(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_to_cart_button)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Add to Cart button")
            raise

    def click_load_more(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.load_more_button)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Load More button")
            raise

    def click_login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_link)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Login link")
            raise

    def click_register(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.register_link)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Register link")
            raise

    def click_home(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.home_link)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Home link")
            raise

    def click_profile(self):
        """Nhấn nút 'Profile'."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.profile_link)
            ).click()
        except TimeoutException:
            print("❌ Timeout waiting for Profile button")
            raise

    def is_add_to_basket_button_displayed(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.add_to_basket_button)
            ).is_displayed()
        except TimeoutException:
            print("❌ Add to Basket button not visible")
            return False

    def is_add_to_cart_button_displayed(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.add_to_cart_button)
            ).is_displayed()
        except TimeoutException:
            print("❌ Add to Cart button not visible")
            return False

    def is_load_more_button_displayed(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.load_more_button)
            ).is_displayed()
        except TimeoutException:
            print("❌ Load More button not visible")
            return False

    def get_product_title(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.product_title)
            ).text
        except TimeoutException:
            print("❌ Product title not visible")
            return ""

    def get_product_time(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.product_time)
            ).text
        except TimeoutException:
            print("❌ Product time not visible")
            return ""

    def get_product_price(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.product_price)
            ).text
        except TimeoutException:
            print("❌ Product price not visible")
            return ""

    def get_basket_count(self):
        try:
            text = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.basket_count)
            ).text
            return int(text.split('(')[1].split(')')[0]) if '(' in text else 0
        except TimeoutException:
            print("❌ Basket count not visible")
            return 0

    def get_cart_count(self):
        try:
            text = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.cart_count)
            ).text
            return int(text.split('(')[1].split(')')[0]) if '(' in text else 0
        except TimeoutException:
            print("❌ Cart count not visible")
            return 0

    def wait_for_load_more_results(self):
        try:
            initial_count = len(self.driver.find_elements(By.CSS_SELECTOR, "div.css-8atqhb"))
            self.click_load_more()
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "div.css-8atqhb")) > initial_count
            )
            print("✅ New content loaded successfully")
            return True
        except TimeoutException:
            print("❌ New content did not load")
            return False