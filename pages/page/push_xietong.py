# _*_coding: utf-8 _*_
# @Time     :2020/2/11  14:30
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :push_fujian.py
# 上传文件
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ActionChains
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage
import win32gui
import win32con


# 主页项目搜索
class PushFile(BasePage):
    def push_file(self, locat):
        company = self.wait_clickable_element((By.XPATH, locat))
        company.click()
        time.sleep(2)
        shangchuan_10 = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[1]/div[2]/div/ul/li[3]/span'))
        shangchuan_10.click()
        shangchuan_11 = self.wait_clickable_element((By.XPATH, '//a[text()="导入"]'))
        shangchuan_11.click()
        shangchuan_12 = self.wait_clickable_element((By.XPATH, '//span[text()="导入申报表"]'))
        shangchuan_12.click()
        shangchuan_13 = self.wait_clickable_element((By.XPATH, '//*[@id="partImport"]/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]/button/span'))
        shangchuan_13.click()
        time.sleep(2)
        # 找到对应的窗口
        self.push()
        time.sleep(3)
        commbit = self.wait_clickable_element((By.XPATH, '//span[text()="提交"]'))
        commbit.click()
        queren = self.wait_clickable_element((By.XPATH, '//a[text()="确认"]'))
        queren.click()


if __name__ == '__main__':
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("18611815532", "222222", "1111")
    time.sleep(3)
    # 搜索项目
    # 单位名称
    locat = '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[1]/span[2]/span'
    project_name = ReadCong().read_conf()
    IndexPage(driver).search(project_name)
    # 上传
    PushFile(driver).push_file(locat)