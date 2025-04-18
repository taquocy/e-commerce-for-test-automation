from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Truy cập trang VnExpress
driver.get("https://vnexpress.net/")
time.sleep(3)  # Đợi trang load (nên dùng WebDriverWait nếu chuyên sâu hơn)

titles = driver.find_elements(By.XPATH, '//h3[@class="title-news"]/a')

for index, title in enumerate(titles, start=1):
    print(f"{index}. {title.text}")
    print(f"XPath: {driver.execute_script('return arguments[0].getAttribute(\"outerHTML\");', title)}")
    print('-' * 50)

# Đóng trình duyệt
driver.quit()
