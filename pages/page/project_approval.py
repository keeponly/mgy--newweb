# _*_coding: utf-8 _*_
# @Time     :2020/2/4  9:48
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :project_approval.py
'''立项审核'''
# 立项提交审核
from mgy.pages.common.read_conf import ReadCong

'''
1.前置条件，项目提交立项
'''
# 提交立项封装成函数
from pages.common.base import BasePage
import time
from selenium import webdriver
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
# 项目信息编辑
from pages.common.zlpg_home import IndexPage
from pages.page.creat_project import CreatPage
from pages.page.login import LoginPage


class ProjectApproval(BasePage):
    def pro_app(self, project_name):
        aduit_ele = IndexPage(self.driver).audit()
        time.sleep(2)
        aduit_ele.click()
        first_ele = self.wait_clickable_element((By.XPATH, '//span[text() = "初审"]'))
        first_ele.click()
        ele_name = '//input[@placeholder="请输入项目名称"]'
        #搜索项目名称
        self.click_send(ele_name, project_name)
        #点击搜索
        reach_ele = self.wait_clickable_element((By.XPATH, '//button[@class="search-btn"]'))
        reach_ele.click()
        #进入项目
        pro_ele = self.wait_clickable_element((By.XPATH, '//div[@title="{}"]'.format(project_name)))
        pro_ele.click()
        submit_ele = self.wait_clickable_element((By.XPATH, '//div[@class="confirm search-btn"]'))
        submit_ele.click()
        confirm_ele = self.wait_clickable_element((By.XPATH, '//span[@class="search-btn"]'))
        confirm_ele.click()
        confirm_ele_01 = self.wait_clickable_element((
                By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]'))
        confirm_ele_01.click()
        driver.quit()

    # 点击编辑


if __name__ == '__main__':
    driver = Chrome()
    LoginPage(driver).login("13511066395", "222222", "1111")
    time.sleep(2)
    project_name = ReadCong().read_conf()
    ProjectApproval(driver).pro_app(project_name)

