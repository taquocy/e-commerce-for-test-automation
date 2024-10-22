import unittest
import configparser
from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.login_page import LoginPage



class CreateNewProductTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

    def test_creat_new_product_successfully(self):
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        create_new_product_page= admin_page.open_new_product_page()
        create_new_product_page.enter_title("IPhone 16 Pro Max")
        create_new_product_page.enter_description("This is Iphone 16 made in China")
        create_new_product_page.enter_price("3000")
        create_new_product_page.click_add_product()



    def tearDown(self):
        return ""
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()
