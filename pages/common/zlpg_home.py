# _*_coding: utf-8 _*_
# @Time     :2020/1/16  11:02
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :home.py
# 首页
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage


# 首页元素定位
class IndexPage(BasePage):
    # 登陆人信息
    def get_user_info(self):
        user_ele = self.wait_find_element((By.XPATH, '//li[@class="userName"]'))
        return user_ele

# 主页按钮
    def home(self):
        home_ele = self.wait_clickable_element((By.XPATH, "i[@class='iconfont icon-zhuye']"))
        return home_ele

# 代办//
    def agent(self):
        agent_ele = self.wait_clickable_element((By.XPATH, "i[@class='iconfont icon-daiban']"))
        return agent_ele

#  项目
    def project(self):
        project_ele = self.wait_find_element((By.XPATH, '//*[@class="iconfont icon-xiangmu"]'))
        return project_ele

# 审核
    def audit(self):
        audit_ele = self.wait_clickable_element((By.XPATH, '//i[@class="iconfont icon-shenhe"]'))
        return audit_ele

# 任务
    def task(self):
        task_ele = self.wait_clickable_element((By.XPATH, '//*[@class="iconfont icon-xiangmu"]'))
        return task_ele

# 管理 class="iconfont icon-guanli"
    def management(self):
        management_ele = self.wait_clickable_element((By.XPATH, '//*[@class="iconfont icon-guanli"]'))
        return management_ele

# 退出//li[text()='退出']
    def exit(self):
        exit_ele = self.wait_clickable_element((By.XPATH, '//li[text()="退出"]'))
        return exit_ele

# 创建项目按钮
    def creat_project(self):
        creat_ele = self.wait_clickable_element((By.XPATH, "//a[text()= '快速创建项目']"))
        time.sleep(2)
        return creat_ele

# 确认项目是否创建成功信息提示
    def message(self, locator) -> WebElement:
        message = self.wait_find_element(
            (By.XPATH, locator))
        return message

#  输入框搜索项目
    def search_project(self):
        return self.wait_clickable_element((By.XPATH, "//input[@placeholder='请输入项目名称关键字']"))

    # 搜索项目，点击搜索,并点击搜索出来的项目
    def click_search(self, project_name):
        # 点击搜索
        res_name_01 = self.wait_clickable_element((By.XPATH, '//i[@class="iconfont icon-sousuo"]'))
        res_name_01.click()
        # 点击出来的项目名称
        locator = "//span[@title = '{}' ]".format(project_name)
        pro_name = self.wait_clickable_element((By.XPATH, locator))
        pro_name.click()
        time.sleep(5)

    # 清除搜索出入框
    def clear_verification_info(self):
        return self.search_project().clear()

    def del_01(self):
        # 定位项目
        res_name_04 = self.wait_find_element(
            (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/span'))
        res_name_04.click()
        time.sleep(1)
        # 删除
        res_name_04 = self.wait_find_element(
            (By.XPATH, '//*[@class="shanChu search-btn fl"]'))
        res_name_04.click()
        time.sleep(1)
        # 返回
        res_name_05 = self.wait_find_element(
            (By.XPATH, '//div[@class="search-btn"]'))
        res_name_05.click()
        time.sleep(1)