from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Cấu hình trình duyệt
options = Options()
options.add_argument("--headless")  # Chạy ẩn không mở trình duyệt
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Khởi động trình duyệt Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Mở trang web VNExpress - chuyên mục Khoa học
url = "https://vnexpress.net/khoa-hoc"
driver.get(url)

# Lấy danh sách các bài viết
articles = driver.find_elements(By.CLASS_NAME, "title-news")

data = []
for article in articles:
    title = article.text  # Tiêu đề bài viết
    link = article.find_element(By.TAG_NAME, "a").get_attribute("href")  # Link bài viết
    data.append({"title": title, "link": link})

# Đóng trình duyệt
driver.quit()

# In kết quả
for item in data:
    print(item)
