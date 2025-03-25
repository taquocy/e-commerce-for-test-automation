from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

### DEFINE CONSTATN
# URL_CRAWL = "https://batdongsan.com.vn/nha-dat-ban-da-nang"
# https://batdongsan.com.vn/nha-dat-ban-buon-ma-thuot-ddl
URL_CRAWL = "https://batdongsan.com.vn/nha-dat-ban-buon-ma-thuot-ddl"
CSS_SELECT_NAVIGATE_ITEM = ".background-pager-right-controls a:nth-last-child(3) div"

## INIT WEB DRIVER : CHROME


# Cách mới để khởi tạo driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(6) 

DEBUG_MODE = True

COUNT = 1
MAX = 303

driver.get(URL_CRAWL + "/p"+ str(COUNT))
## COMMON FUNCTIONS
def check_exists_by_xpath(cssSelector):
    try:
        driver.find_element(By.CSS_SELECTOR,cssSelector)
    except NoSuchElementException:
        return False
    return True

#### MAIN FUNCTION

try:
    print('Connect DB')
    # FINAL DATA
    connection = mysql.connector.connect(host='localhost',
                                         database='bds_crawl',
                                         user='root',
                                         password='Y649394$')
    if (DEBUG_MODE == True):
        # TEMP TEST TABLE ABD DATA
        connection = mysql.connector.connect(host='localhost',
                                             database='bds_test',
                                             user='root',
                                             password='Y649394$')


    while True :
        print('OOOOOKKKKK')
        COUNT = COUNT + 1
        if COUNT == MAX :
            break
                

        listItem = driver.find_elements(By.CSS_SELECTOR,'.js__product-link-for-product-id')
        
        for item in listItem:
            try :

                title = item.find_element(By.CSS_SELECTOR,'.re__card-info .re__card-info-content .re__card-title .js__card-title').text
                print(title)

                price = item.find_element(By.CSS_SELECTOR,'.re__card-info .re__card-info-content .re__card-config .re__card-config-price').text
                print(price)

                description = ""
                # Du lieu moi ko co description
                # description = item.find_element_by_css_selector('.re__card-info .re__card-info-content .re__card-description.js__card-description').text
                # print(description)

                distCity = item.find_element(By.CSS_SELECTOR,'.re__card-info .re__card-info-content .re__card-location').text
                print(distCity)

                uptime = datetime.date.today()
                try:
                    uptime = item.find_element(By.CSS_SELECTOR,'.re__card-info .re__card-published-info  span.re__card-published-info-published-at').get_attribute('aria-label')
                    print(uptime)
                except NoSuchElementException:
                    print('can get the data up-time')

                productArea = item.find_element(By.CSS_SELECTOR,'.re__card-info .re__card-info-content .re__card-config .re__card-config-area').text
                print(productArea)
                
                #photoSample = item.find_element_by_css_selector('.product-avatar-img').get_attribute('src')
                photoSample = ''
                print(photoSample)

                # FILTER - INVALID DATA


                # INSERT INTO DB
                mySql_insert_query = """INSERT INTO BATDONGSAN ( title, description, image, uptime, price, distcity, space) 
                            VALUES 
                            (%s, %s, %s, %s, %s, %s, %s) """

                insert_tuple_ = (title, description, photoSample, uptime, price, distCity, productArea)

                cursor = connection.cursor()
                cursor.execute(mySql_insert_query, insert_tuple_)
    
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into Laptop table")
                cursor.close()
                
            except NoSuchElementException:
                print('ERROR')
                continue    

        driver.close()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.implicitly_wait(6) 
        driver.get(URL_CRAWL + "/p"+ str(COUNT))


        # navigateItem = driver.find_element_by_css_selector(CSS_SELECT_NAVIGATE_ITEM)        
        # navigateItem.click()


    # CLOSE DRIVER
    #driver.close()    


except mysql.connector.Error as error:
    print("Failed to insert record into BDS table {}".format(error))

finally:    
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

# # CLOSE DRIVER
# driver.close()
