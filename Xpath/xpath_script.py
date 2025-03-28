from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi động trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://demoqa.com/automation-practice-form")

# Chờ tối đa 10 giây để phần tử xuất hiện
wait = WebDriverWait(driver, 10)

# Tìm ô nhập "First Name" sau khi đảm bảo nó đã xuất hiện
name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']")))
name_field.send_keys("Nguyen Van A")

# Điền vào ô "Last Name"
last_name_field = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='lastName']")))
last_name_field.send_keys("Test")

# Điền vào ô "Email"
email_field = driver.find_element(By.XPATH, "//*[@id='userEmail']")
email_field.send_keys("testemail@example.com")

# Điền vào ô "Mobile Number"
phone_field = driver.find_element(By.XPATH, "//*[@id='userNumber']")
phone_field.send_keys("0123456789")

# Đóng trình duyệt sau khi hoàn thành
driver.quit()
