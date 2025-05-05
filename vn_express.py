from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Thiết lập Chrome chạy không hiển thị (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")  

# Khởi tạo trình duyệt với WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Mở trang VnExpress - Thể thao
url = "https://vnexpress.net/the-thao"
driver.get(url)

# In tiêu đề trang
print("Tiêu đề trang:", driver.title)

# Lấy danh sách tiêu đề bài báo thể thao
articles = driver.find_elements(By.CSS_SELECTOR, "h3.title-news a")

print("\nDanh sách bài viết thể thao:")
for idx, article in enumerate(articles[:10], start=1):  # Lấy 10 bài đầu tiên
    print(f"{idx}. {article.text} - {article.get_attribute('href')}")

# Đóng trình duyệt
driver.quit()
