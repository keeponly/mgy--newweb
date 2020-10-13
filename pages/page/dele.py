# _*_coding: utf-8 _*_
# @Time     :2020/1/18  14:31
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :dele.py
import time
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage
from mgy.pages.common.zlpg_home import IndexPage
'''未立项项目删除
搜索未立项单位，进入未立项单位页面'''


class DelProject(BasePage):
    # 进入项目
    def del_pro(self, name):

        # 点击项目
        search_ele = IndexPage(self.driver).project()
        time.sleep(1)
        search_ele.click()

    # 我负责的
        time.sleep(1)
        res_name_01 = self.wait_find_element((
            By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/ul/li[2]'))
        res_name_01.click()
        time.sleep(1)

    # 输入项目名称
        res_name_04 = self.wait_find_element((By.XPATH, '//input[@placeholder="请输入项目名称"]'))
        res_name_04.click()
        res_name_04.send_keys(name)
        time.sleep(1)

        # 搜索
        res_name_03 = self.wait_find_element((By.XPATH, '//button[@class="search-btn"]'))
        res_name_03.click()
        time.sleep(1)

        # 立项中
        res_name_03 = self.wait_find_element((By.XPATH, '//*[@id="tab-setup"]'))
        res_name_03.click()
        time.sleep(1)



