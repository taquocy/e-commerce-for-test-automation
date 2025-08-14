from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://e-commerce-for-testing.onrender.com")

# Đăng nhập
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("superadmin@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()




# Chuyển đến trang quản lý sản phẩm
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Products') or contains(@href, '/products')]"))).click()
except:
    driver.get("https://e-commerce-for-testing.onrender.com/admin/products")  # Fallback URL

# Chọn sản phẩm đầu tiên để chỉnh sửa
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//button[contains(text(), 'Edit')])[1]"))).click()

# Chờ trang Update Product load xong
update_form = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[contains(@class, 'update-form')]")))

# Lấy tất cả elements trong form update
form_elements = update_form.find_elements(By.XPATH, ".//*")

# In thông tin các elements
for idx, element in enumerate(form_elements, 1):
    try:
        xpath = driver.execute_script("""
            function getElementXPath(element) {
                if (element.id) return '//*[@id="' + element.id + '"]';
                let paths = [];
                for (; element && element.nodeType === 1; element = element.parentNode) {
                    let index = 0;
                    for (let sibling = element.previousSibling; sibling; sibling = sibling.previousSibling) {
                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) index++;
                    }
                    let tagName = element.tagName.toLowerCase();
                    let pathIndex = (index ? "[" + (index + 1) + "]" : "");
                    paths.unshift(tagName + pathIndex);
                }
                return paths.length ? "/" + paths.join("/") : null;
            }
            return getElementXPath(arguments[0]);
        """, element)
        
        print(f"{idx}. Tag: {element.tag_name}")
        print(f"   XPath: {xpath}")
        print(f"   Text: {element.text[:30]}" if element.text else "")
        print(f"   Type: {element.get_attribute('type')}")
        print(f"   Name: {element.get_attribute('name')}")
        print("-" * 60)
    except Exception as e:
        print(f"Error with element {idx}: {str(e)}")

driver.quit()
# Thay đổi nếu trang web dùng icon hoặc component khác
#XPath cho nút chuyển trang
"(//button[contains(text(), 'Edit')])[1]"
# Thay class 'update-form' bằng class thực tế
#Định danh form update
"//form[contains(@class, 'update-form')]"
# Ví dụ cập nhật giá sản phẩm
#Bạn có thể thêm các thao tác cập nhật sản phẩm như sau sau khi đã có đúng XPath:
price_field = driver.find_element(By.XPATH, "//input[@name='price']")
price_field.clear()
price_field.send_keys("99.99")

# Submit form
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#Để lấy XPath chính xác

#Mở trang web trong Chrome

#Chuột phải vào element cần lấy

#Chọn Inspect

#Chuột phải vào element trong DevTools > Copy > Copy XPath