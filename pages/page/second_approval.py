# _*_coding: utf-8 _*_
# @Time     :2020/2/10  17:34
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :second_approval.py
# 复审
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage
from mgy.pages.page.first_approval import CompanyApproval


class SecondApproval(BasePage):
    def second_approval(self):
        CompanyApproval(self.driver).company_app(project_name)


if __name__ == '__main__':
    driver = Chrome()
    LoginPage(driver).login("13801094545", "222222", "1111")
    time.sleep(2)
    project_name = ReadCong().read_conf()
    SecondApproval(driver).second_approval()