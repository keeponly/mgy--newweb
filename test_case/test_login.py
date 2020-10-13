# _*_coding: utf-8 _*_
# @Time     :2020/1/16  9:59
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_login.py
import ddt
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage
import time
import unittest
from selenium.webdriver import Chrome
from mgy.test_data.project_data import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:  # 只执行一次 所有用例走完来一次
        cls.driver = Chrome()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass
        # self.driver = Chrome()
        # self.login_page = LoginPage(self.driver)

    def tearDown(self) -> None:
        pass

        # self.driver.quit()

    # @ddt.data(*user_info_success)
    def test_login_2_success(self):
        self.login_page.login("18611815532", "222222", "1111")
        user_message = IndexPage(self.driver).get_user_info()
        print(user_message.text)
        self.assertTrue("张倩倩" in user_message.text)

    @ddt.data(*user_info_error)
    def test_login_1_error(self, data):
        self.login_page.login(data['username'], data['password'], data['code'])
        time.sleep(3)
        flash_ele = self.login_page.get_flash_info()
        self.assertTrue(data['expect'] == flash_ele.text)
        self.login_page.clear_pwd_info()
        self.login_page.clear_verification_info()


if __name__ == '__main__':
    unittest.main()
