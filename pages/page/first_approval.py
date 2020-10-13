# _*_coding: utf-8 _*_
# @Time     :2020/2/10  14:49
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :first_approval.py
# 单位送审审核
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage


class CompanyApproval(BasePage):
    def company_app(self, project_name):
        list_01 = [
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/label/span/span',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/label/span/span',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div[2]/div[1]/label/span/span']

        list_02 = ['//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/label[1]/span[1]/span',
                   '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/div/label[1]/span[1]/span',
                   '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[2]/div/label[1]/span[1]/span',
                   '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[2]/div/label[1]/span[1]/span',
                   '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/label[1]/span[1]/span',
                   '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/div/label[1]/span[1]/span',

        ]
        aduit_ele = IndexPage(self.driver).audit()
        time.sleep(2)
        aduit_ele.click()
        time.sleep(2)
        ele_name = '//input[@placeholder="请输入项目名称"]'
        # 搜索项目名称
        self.click_send(ele_name, project_name)
        # 点击搜索
        reach_ele = self.wait_clickable_element((By.XPATH, '//button[@class="search-btn"]'))
        reach_ele.click()
        # 进入项目
        pro_ele = self.wait_clickable_element((By.XPATH, '//span[@title="{}"]'.format(project_name)))
        pro_ele.click()
        try:
            shenhe = self.wait_clickable_element((By.XPATH, '//div[text()="开始审核"]'))
            shenhe.click()
            queding = self.wait_clickable_element((
                By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]'))
            queding.click()
            time.sleep(2)
        except:
            # 批量审核
            edit_ele = self.wait_clickable_element((By.XPATH, '//a[text()="批量审核"]'))
            edit_ele.click()
            self.multiple_click(list_01)
            sub_01 = self.wait_clickable_element((By.XPATH, '//button[text()="审核"]'))
            sub_01.click()
            self.multiple_click(list_02)
            sub_02 = self.wait_clickable_element((By.XPATH, '//a[text()="确定"]'))
            sub_02.click()


if __name__ == '__main__':
    driver = Chrome()
    LoginPage(driver).login("13911419652", "222222", "1111")
    time.sleep(2)
    project_name = ReadCong().read_conf()
    CompanyApproval(driver).company_app(project_name)