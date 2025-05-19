from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Cấu hình WebDriver
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())  # Sử dụng Service

driver = webdriver.Chrome(service=service, options=options)

try:
    # Mở Google
    driver.get("https://www.google.com")
    
    # Kiểm tra tiêu đề trang
    assert "Google" in driver.title
    print(" Trang Google mở thành công!")

    # Tìm ô tìm kiếm và nhập từ khóa
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Chờ một chút để trang kết quả tải xong (tùy chỉnh nếu cần)
    driver.implicitly_wait(5)

    # Kiểm tra kết quả tìm kiếm có xuất hiện không
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, " Không tìm thấy kết quả nào!"

    print(f"Tìm thấy {len(results)} kết quả cho 'Selenium Python'")

finally:
    # Đóng trình duyệt
    driver.quit()
    print("Trình duyệt đã đóng.")
