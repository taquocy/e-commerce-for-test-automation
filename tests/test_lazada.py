from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo Selenium với WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Mở trang Lazada
url = "https://www.lazada.vn/"
driver.get(url)
time.sleep(3)  

# Tìm ô tìm kiếm và nhập từ khóa "đồ chơi" từng chữ một
search_box = driver.find_element(By.NAME, "q")
for char in "chăn gối":
    search_box.send_keys(char)
    time.sleep(0.2)  # Hiệu ứng nhập từng chữ
search_box.send_keys(Keys.ENTER)

time.sleep(5)  # Chờ trang kết quả tải xong

# Lấy danh sách sản phẩm
products = driver.find_elements(By.CLASS_NAME, "Bm3ON")  # Class chứa sản phẩm trên Lazada

for product in products:
    try:
        name = product.find_element(By.CLASS_NAME, "RfADt").text  # Class chứa tên sản phẩm
        price = product.find_element(By.CLASS_NAME, "ooOxS").text  # Class chứa giá sản phẩm
        
        print(f"Tên sản phẩm: {name} - Giá: {price}")
    except Exception as e:
        print("Lỗi lấy dữ liệu sản phẩm:", e)

# Đóng trình duyệt
driver.quit()