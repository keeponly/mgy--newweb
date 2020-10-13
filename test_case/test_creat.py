# _*_coding: utf-8 _*_
# @Time     :2020/1/16  23:02
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :test_creat.py
import time
import unittest
from selenium.webdriver import Chrome
from mgy.pages.page.login import LoginPage
import ddt
from mgy.pages.page.creat_project import CreatPage
from mgy.test_data.project_data import *


@ddt.ddt
class TestCreat(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.creat_project = CreatPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login("18611815532", "222222", "1111")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        # self.driver.quit()
        pass

    #  在首页点击创建项目按钮
    @ddt.data(*creat_project)
    def test_creat_success(self, data):
        # 点击创建项目
        self.creat_project.creat_project()
        # 输入项目名称
        e = self.creat_project.get_input_project_name()
        e.send_keys(data['project_name'])
        # 选择项目类型
        self.creat_project.click_project_type()
        self.creat_project.chose_project_type(data['project_type'])
        # 选择评估基准日
        self.creat_project.click_base_date()
        # 点击评估目的
        self.creat_project.click_purpose_evaluation()
        # 预期合同价
        a = self.creat_project.get_except_price()
        a.send_keys(100)
        # 第一签字评估师
        self.creat_project.first_signer()
        # 第二签字评估师
        self.creat_project.second_signer()
        # 股权结构树
        self.creat_project.equity_tree()
        # 创建
        self.creat_project.establish()
        # 确认
        self.creat_project.confirm()
        time.sleep(2)
    # flash_ele = self.creat_project.get_flash_info()
    # self.assertTrue("请输入必填项" == flash_ele.text)


if __name__ == '__main__':
    unittest.main()
