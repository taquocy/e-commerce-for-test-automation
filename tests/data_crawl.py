import time
import csv
import pyodbc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DataCollector:
    def __init__(self, url, css_selector_name, css_selector_price, db_name):
        self.url = url
        self.css_selector_name = css_selector_name
        self.css_selector_price = css_selector_price
        self.db_name = db_name

    def collect_data(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.url)
        time.sleep(5)

        data = []
        items = driver.find_elements(By.CSS_SELECTOR, '.product-info')
        for item in items:
            try:
                name = item.find_element(By.CSS_SELECTOR, self.css_selector_name).text.strip()
                price = item.find_element(By.CSS_SELECTOR, self.css_selector_price).text.strip()
                data.append((name, price))
                print(f"{name} : {price}")
            except Exception as e:
                print("Error collecting data:", e)

        driver.quit()
        return data

    def save_to_csv(self, data, filename):
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price"])
            writer.writerows(data)
        print(f"Data saved to {filename}")

    


# Example usage
collector = DataCollector(
    url="https://cellphones.com.vn/laptop.html",
    css_selector_name=".product__name",
    css_selector_price=".product__price--show",
  
)

# Collect data and save
data = collector.collect_data()
collector.save_to_csv(data, "product_data.csv")
