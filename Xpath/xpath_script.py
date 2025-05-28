from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name.send_keys("Nguyen")

last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name.send_keys("Van A")

email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.send_keys("test@example.com")

gender = driver.find_element(By.XPATH, "//label[text()='Male']")
gender.click()

phone = driver.find_element(By.XPATH, "//input[@id='userNumber']")
phone.send_keys("0123456789")

dob = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
driver.execute_script("arguments[0].scrollIntoView();", dob)
dob.click()


year = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'react-datepicker__year-select')]"))
)
year.click()
driver.find_element(By.XPATH, "//option[text()='2000']").click()


month = driver.find_element(By.XPATH, "//select[contains(@class,'react-datepicker__month-select')]")
month.click()
driver.find_element(By.XPATH, "//option[text()='January']").click()


day = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']")
day.click()


subject = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)


hobby = driver.find_element(By.XPATH, "//label[text()='Sports']")
hobby.click()


address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
address.send_keys("123 Đường ABC, Quận XYZ, TP HCM")


state = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
state.send_keys("NCR")
state.send_keys(Keys.RETURN)


city = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)


submit = driver.find_element(By.XPATH, "//button[@id='submit']")
driver.execute_script("arguments[0].click();", submit)  

modal = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'modal-content')]")))
assert "Thanks for submitting the form" in modal.text
print("Form đã được submit thành công!")

time.sleep(3)


driver.quit()