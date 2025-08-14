from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.double_click_button = (By.ID, "doubleClickBtn")
        self.right_click_button = (By.ID, "rightClickBtn")
        self.dynamic_click_button = (By.XPATH, "//button[text()='Click Me']")

    def double_click(self):
        from selenium.webdriver.common.action_chains import ActionChains
        action = ActionChains(self.driver)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.double_click_button)
        )
        action.double_click(button).perform()

    def right_click(self):
        from selenium.webdriver.common.action_chains import ActionChains
        action = ActionChains(self.driver)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.right_click_button)
        )
        action.context_click(button).perform()

    def dynamic_click(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dynamic_click_button)
        )
        button.click()