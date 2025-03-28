from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Khởi tạo trình điều khiển Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Truy cập trang web
url = "https://laptopaz.vn/laptop-gaming.html"
driver.get(url)
driver.implicitly_wait(5)  # Đợi phần tử tải lên

# Danh sách chứa thông tin sản phẩm
products = []

# Tìm tất cả sản phẩm trong danh sách
product_elements = driver.find_elements(By.XPATH, "//*[@id='product']/div")

for index, product in enumerate(product_elements, start=1):
    try:
        # XPath động theo index
        name_xpath = f"//*[@id='product']/div[{index}]/div[2]/a"
        price_xpath = f"//*[@id='product']/div[{index}]/div[2]/span/span/span[1]"
        discount_xpath = f"//*[@id='product']/div[{index}]/span/span"

        # Lấy thông tin sản phẩm
        name = product.find_element(By.XPATH, name_xpath).text
        price = product.find_element(By.XPATH, price_xpath).text
        try:
            discount = product.find_element(By.XPATH, discount_xpath).text
        except:
            discount = "Không có giảm giá"

        products.append({
            "Tên sản phẩm": name,
            "Giá": price,
            "Giảm giá": discount
        })
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu sản phẩm thứ {index}: {e}")

# In kết quả
for product in products:
    print(product)

# Đóng trình duyệt
driver.quit()
