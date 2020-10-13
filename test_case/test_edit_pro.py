# _*_coding: utf-8 _*_
# @Time     :2020/1/18  13:41
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :test_edit_pro.py
import time
import unittest
from selenium.webdriver import Chrome
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.edit_project import EditProject
from mgy.pages.page.login import LoginPage
import ddt
from mgy.test_data.project_data import *

# 测试项目信息编辑
# 登录--搜索项目--点击项目


@ddt.ddt
class TestEditPro(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.edit_project = EditProject(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login("18611815532", "222222", "1111")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        IndexPage(self.driver).clear_verification_info()

    @ddt.data(*edit_project)
    def test_edit_success(self, data):
        # 点击主页项目搜索项目
        click_search_ele = IndexPage(self.driver).search_project()
        # 发送项目名称
        click_search_ele.send_keys(data['project_name'])

        IndexPage(self.driver).click_search(data['project_name'])



if __name__ == '__main__':
    unittest.main()
