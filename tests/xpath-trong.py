from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("chromedriver"))
driver.get("https://demoqa.com/text-box")

el = driver.find_element(By.ID, "userName")

# Lấy XPath không dùng function
xpath = driver.execute_script("""
let el = arguments[0];
let path = '';
while (el && el.nodeType === 1) {
  let index = 1, sib = el.previousElementSibling;
  while (sib) {
    if (sib.tagName === el.tagName) index++;
    sib = sib.previousElementSibling;
  }
  path = '/' + el.tagName.toLowerCase() + '[' + index + ']' + path;
  el = el.parentElement;
}
return path;
""", el)

print("XPath:", xpath)
driver.quit()
