# _*_coding: utf-8 _*_
# @Time     :2020/2/4  10:15
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :mode_management.py
# 项目模式管理 附件，协同，混合
'''
登录管理员账号
点击管理
点击项目模式管理
点击全部
搜索输入项目
点击搜索
点击搜索的项目
点击部分协同
确认人--备注--确认--确认
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ActionChains
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage


class ModeManagement(BasePage):
    def mode_management(self, project_name):
        """点击管理"""
        mode_manage = IndexPage(self.driver).management()
        mode_manage.click()
        """项目模式管理"""
        pattern_ele = self.wait_clickable_element((By.XPATH,'//a[text()="项目模式管理"]'))
        pattern_ele.click()
        """//span[text()="全部"]"""
        all_ele = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/label[4]/span[1]/span'))
        all_ele.click()
        pro_name_ele = self.wait_clickable_element((By.XPATH, '//input[@placeholder="请输入项目名称"]'))
        pro_name_ele.click()
        pro_name_ele.send_keys(project_name)
        """搜索"""
        search_ele = self.wait_clickable_element((By.XPATH, '//button[@class="search-btn"]'))
        search_ele.click()
        time.sleep(2)
        """点击搜索出的项目"""
        project_ele = self.wait_clickable_element((By.XPATH, '//div[@title="{}"]'.format(project_name)))
        project_ele.click()
        '''部分协同'''
        part_ele = self.wait_clickable_element((
            By.XPATH, '//*[@id="pane-first"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/label[2]/span[2]'))
        part_ele.click()
        Drag_01 = self.wait_clickable_element((
            By.XPATH,
            '//*[@id="pane-first"]/div/div[1]/div/div[2]/div/div'))
        ActionChains(self.driver).drag_and_drop_by_offset(Drag_01, 0, 100).perform()

        list_01 =[
           "//*[@id='pane-first']/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/div/span[3]/span",
           '//*[@id="pane-first"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[1]/div/span[3]/span',
           '//*[@id="pane-first"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[2]/div/span[3]/span',
           '//*[@id="pane-first"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/div[3]/div/span[3]/span',
           '//*[@id="pane-first"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div[3]/table/tbody/tr[5]/td[1]/div/div/div/span[3]/span']

        for i in list_01:
            ele_01 = self.wait_clickable_element((By.XPATH, i))
            ele_01.click()

        applicant = self.wait_clickable_element((By.XPATH, "//input[@placeholder='请输入申请人']"))
        applicant.click()
        applicant_01 = self.wait_clickable_element((
            By.XPATH, '//*[@id="pane-first"]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]'))
        applicant_01.click()
        applicant_02 = self.wait_clickable_element((By.XPATH, '//a[text()="确定"]'))
        applicant_02.click()
        applicant_03 = self.wait_clickable_element((
            By.XPATH, '//textarea[@class="el-textarea__inner"]'))
        applicant_03.click()
        applicant_03.send_keys(123)
        applicant_04 = self.wait_clickable_element((By.XPATH, '//a[text()="确认提交"]'))
        applicant_04.click()
        applicant_05 = self.wait_clickable_element((By.XPATH, '//div[text()="确定"]'))
        applicant_05.click()


if __name__ == '__main__':
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("13600001111", "222222", "1111")
    time.sleep(3)
    project_name = ReadCong().read_conf()
    ModeManagement(driver).mode_management(project_name)