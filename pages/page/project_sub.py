# _*_coding: utf-8 _*_
# @Time     :2020/2/10  13:38
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :project_sub.py
# 项目送审
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage
'''
//a[text()="批量送审"]
项目选择
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/label/span/span',
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/label/span/span',
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div[2]/div[1]/label/span/span'
/button[text()="送审"]
附件1
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/div/div/input'
附件2
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/div/div/div/input'
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div/div/div/input'
//a[text()="确定"]
滚动条
'//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]'
'''
class ProjectSub(BasePage):

    def project_sub(self):

        list_01 = ['//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/label/span/span',
                  '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/label/span/span',
                  '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div[2]/div[1]/label/span/span']

        list_02 = [
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div/div/div/input'
        ]

        edit_ele = self.wait_clickable_element((By.XPATH, '//a[text()="批量送审"]'))
        edit_ele.click()
        self.multiple_click(list_01)
        sub_01 = self.wait_clickable_element((By.XPATH, '//button[text()="送审"]'))
        sub_01.click()
        Drag_01 = self.wait_clickable_element((
            By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]'))
        ActionChains(self.driver).drag_and_drop_by_offset(Drag_01, 500, 0).perform()
        self.multiple_send(list_02)
        sub_02 = self.wait_clickable_element((By.XPATH, '//a[text()="确定"]'))
        sub_02.click()


if __name__ == '__main__':

    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("18611815532", "222222", "1111")
    project_name = ReadCong().read_conf()
    IndexPage(driver).search(project_name)
    ProjectSub(driver).project_sub()

