from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class text_box:
    def __init__(self, driver):
        self.driver = driver

        self.fullname = (By.XPATH, "//*[@id='userName']")
        self.email = (By.XPATH, "//*[@id='userEmail']")
        self.address = (By.XPATH, "//*[@id='currentAddress']")
        self.paddress = (By.XPATH, "//*[@id='permanentAddress']")
        self.submit = (By.XPATH, "//button[@id='submit']")

    def enter_fullname(self, fullname):
        self.driver.find_element(*self.fullname).send_keys(fullname)

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    def enter_paddress(self, paddress):
        self.driver.find_element(*self.paddress).send_keys(paddress)

    def click_submit(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.submit)
        )
        self.driver.find_element(*self.submit).click()