from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang Home
        self.add_to_basket_button = (By.XPATH, "//button[contains(text(),'Add to Basket')]")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(),'Add to cart')]")
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
            load_more_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Load More']"))
            )
            load_more_button.click()
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
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'chakra-card')]"))
            )
            print("New content loaded successfully!")
            return True
        except TimeoutException:
            print("Error: New content did not load within the timeout.")
            return False
    
    def test_load_more(self):
        try:
            initial_count = len(self.driver.find_elements(By.XPATH, "//div[contains(@class, 'chakra-card')]"))
            print(f"Initial content count: {initial_count}")

            self.click_load_more()
            print("Clicked 'Load More' button.")

            if self.wait_for_load_more_results():

                WebDriverWait(self.driver, 10).until(
                    lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'chakra-card')]")) > initial_count
                )

                final_count = len(self.driver.find_elements(By.XPATH, "//div[contains(@class, 'chakra-card')]"))
                print(f"Final content count: {final_count}")
                   
                if final_count > initial_count:
                    print("Test passed: Load More button is working.")
                    return True
                else:
                    print("Test failed: No new content loaded.")
                    return False
            else:
                print("Test failed: No new content detected after clicking 'Load More'.")

        except Exception as e:
            print(f"Test failed due to an error: {e}")
            return False

    def test_toggle_basket_button(self):
        try:
            add_to_basket_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Basket')]")
            add_to_basket_button.click()
            print("Clicked 'Add to Basket' button.")

            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, "//button[contains(text(), 'Remove from Basket')]"), "Remove from Basket")
            )

            remove_from_basket_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Remove from Basket')]")
            if remove_from_basket_button:
                print("Test passed: Button changed to 'Remove from Basket'.")
            else:
                print("Test failed: Button did not change to 'Remove from Basket'.")
                return False

            remove_from_basket_button.click()
            print("Clicked 'Remove from Basket' button.")

            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, "//button[contains(text(), 'Add to Basket')]"), "Add to Basket")
            )

            add_to_basket_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Basket')]")
            if add_to_basket_button:
                print("Test passed: Button changed back to 'Add to Basket'.")
                return True
            else:
                print("Test failed: Button did not change back to 'Add to Basket'.")
                return False

        except Exception as e:
            print(f"Test failed due to an error: {e}")
            return False
        
    def test_navigate_to_item_detail(self):
        try:
            first_item = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'chakra-card')]//a)[1]")
            item_link = first_item.get_attribute("href") 
            first_item.click()
            print("Clicked on item.")

            current_url = self.driver.current_url

            if item_link in current_url:
                print("Test passed: Successfully navigated to item detail page.")
                return True
            else:
                print(f"Test failed: Expected {item_link} but got {current_url}")
                return False
        except Exception as e:
            print(f"Test failed due to an error: {e}")
            return False
