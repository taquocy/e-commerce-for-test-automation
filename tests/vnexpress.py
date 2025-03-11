from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Cài đặt trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Mở trang Thể thao của VnExpress
driver.get("https://vnexpress.net/the-thao")

titles = driver.find_elements(By.CSS_SELECTOR, "h3.title-news a")

# Lọc bỏ các tiêu đề trống và in tiêu đề ra console
filtered_titles = [title.text.strip() for title in titles if title.text.strip()]

for index, title in enumerate(filtered_titles, 1):
    print(f"{index}. {title}")

# Đóng trình duyệt
driver.quit()
