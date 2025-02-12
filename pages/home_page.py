# # from selenium.webdriver.common.by import By

# # class HomePage:
# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.login_button = (By.XPATH, "//button[contains(text(), 'Login')]")
# #         self.register_button = (By.XPATH, "//button[contains(text(), 'Register')]")
# #         self.product_card = (By.XPATH, "//img[@alt='Product']")  
# #         self.product_title = (By.XPATH, "//div[@id='content']//h2")
# #         self.product_time = (By.XPATH, "//div[@id='content']//p[1]")
# #         self.product_price = (By.XPATH, "//div[@id='content']//p[2]")
# #         self.add_to_basket_button = (By.XPATH, "//div[@id='content']//button[1]")
# #         self.add_to_cart_link = (By.XPATH, "//div[@id='content']//button[2]")
 
# #     def click_login(self):
# #         self.driver.find_element(*self.login_button).click()

# #     def click_register(self):
# #         self.driver.find_element(*self.register_button).click()

# #     def click_add_to_basket(self):
# #         self.driver.find_element(*self.add_to_basket_button).click()

# #     def click_add_to_cart(self):
# #         self.driver.find_element(*self.add_to_cart_link).click()

# #     def get_product_title(self):
# #         return self.driver.find_element(*self.product_title).text

# #     def get_product_time(self):
# #         return self.driver.find_element(*self.product_time).text

# #     def get_product_price(self):
# #         return self.driver.find_element(*self.product_price).text


# from selenium.webdriver.common.by import By

# class HomePage:
#     def __init__(self, driver):
#         self.driver = driver

#         # Define the selector for the "Add to Basket" button
#         # Update the XPath below based on the actual "Add to Basket" button's location on your home page
#         self.add_to_basket_button = (By.XPATH, "//*[@id='content']/div/div[1]/div/div[1]/div/div/div/button[1]")

#     # Method to add an item to the basket
#     def add_item_to_basket(self):
#         self.driver.find_element(*self.add_to_basket_button).click()
