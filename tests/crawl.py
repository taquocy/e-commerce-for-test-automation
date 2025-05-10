import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Khởi tạo trình điều khiển
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL trang Dantri
url = 'https://dantri.com.vn/'
driver.get(url)

# Chờ các bài viết tải xong
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'article'))
)

# Lấy danh sách bài viết
articles = driver.find_elements(By.CSS_SELECTOR, 'article')

# Danh sách lưu dữ liệu
data = []

# Duyệt qua từng bài viết và trích xuất thông tin
for article in articles:
    try:
        # Tiêu đề bài viết
        title_element = article.find_element(By.CSS_SELECTOR, 'h3 a')
        title = title_element.text.strip()
        # Link bài viết
        link = title_element.get_attribute('href')
        # Mô tả (nếu có)
        description_elements = article.find_elements(By.CSS_SELECTOR, 'div.sapo')
        description = description_elements[0].text.strip() if description_elements else 'Không có mô tả'

        # Lưu thông tin vào danh sách
        data.append({
            'Tiêu đề': title,
            'Link': link,
            'Mô tả': description
        })

        # In thông tin ra console (nếu cần)
        print(f'Tiêu đề: {title}\nLink: {link}\nMô tả: {description}\n{"-"*60}')
    except Exception as e:
        # Bỏ qua nếu có lỗi trích xuất bài viết cụ thể
        continue

# Đóng trình duyệt
driver.quit()

# Xuất dữ liệu ra file CSV
output_file = 'dantri_baiviet.csv'

# Định nghĩa header
header = ['Tiêu đề', 'Link', 'Mô tả']
