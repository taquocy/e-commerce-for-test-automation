from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Cấu hình trình duyệt
options = Options()
options.add_argument("--start-maximized")

service = Service(executable_path="chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://demoqa.com")

    time.sleep(3) 

    elements = driver.find_elements(By.CLASS_NAME, "card")

    print("==> Các XPath của phần tử chính trên trang chủ DemoQA:")
    for index, el in enumerate(elements, start=1):
        xpath = f"(//div[@class='card'])[{index}]"
        title = el.text.replace("\n", " - ")
        print(f"{index}. {title} => {xpath}")

finally:
    driver.quit()
