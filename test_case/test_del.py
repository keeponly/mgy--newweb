# _*_coding: utf-8 _*_
# @Time     :2020/1/18  15:48
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :test_del.py
import unittest
from selenium.webdriver import Chrome
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage
from mgy.pages.page.dele import DelProject


class TestCreat(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        name = "33"
        cls.driver = Chrome()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login("18610933265", "222222", "1111")
        DelProject(cls.driver).del_pro(name)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        # self.driver.quit()
        pass

    #  在首页点击创建项目按钮

    def test_del(self):
        for i in range(100):
            IndexPage(self.driver).del_01()


if __name__ == '__main__':
    unittest.main()
