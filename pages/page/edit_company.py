# _*_coding: utf-8 _*_
# @Time     :2020/2/4  16:19
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :edit_company.py
# 公司信息编辑
'''进入项目，点击编辑，输入公司信息，点击确认'''
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage
from mgy.pages.common.read_conf import ReadCong
from mgy.pages.common.zlpg_home import IndexPage
from mgy.pages.page.login import LoginPage


class Company(BasePage):
    def edit_company(self):
        # 展开单位
        fen_ele = self.wait_clickable_element((By.XPATH, '//span[text()="分"]'))
        fen_ele.click()
        time.sleep(5)
        # 公司定位一级单位
        list_01 = ['//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/div[1]/span[2]/span',
                   '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/span[2]/span',
                   '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[2]/div[2]/div/div[1]/span[2]/span']
        # 公司定位二级单位
        list_02 = [
            '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/span[2]/span',
            '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/span[2]/span',
            '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/span[2]/span']
        # 一级单位三法选择
        list_03 = [
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[1]/div/div[1]/div/div/div/label[1]/span[2]',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[1]/div/div[1]/div/div/div/label[2]/span[2]',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[1]/div/div[1]/div/div/div/label[3]/span[2]', ]
        # 二级单位三法选择
        list_06 = [
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div/div[2]/div[1]/div/div[1]/div/div/div/label[1]/span[2]',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div/div[2]/div[1]/div/div[1]/div/div/div/label[2]/span[2]',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div/div[2]/div[1]/div/div[1]/div/div/div/label[3]/span[2]']

        # 一级所有点击后输入的元素
        list_04 = [
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[1]/div/div[4]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[2]/div/div[1]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[2]/div/div[8]/div/div/div/input']

        #  二级所有点击后输入的元素
        list_05 = [
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div[4]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[1]/div/div/div/input',
            '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[8]/div/div/div/input']

#一级单位编辑

        for i in list_01:
            # 选择单位
            company_ele = self.wait_clickable_element((By.XPATH, i))
            company_ele.click()
            time.sleep(3)
            rule_el = self.wait_clickable_element((By.XPATH, '//span[text()="+ 请选择作价模板"]'))
            rule_el.click()
            rule_el_01 = self.wait_clickable_element((By.XPATH, '//div[@class="template-con fs13"]'))
            rule_el_01.click()
            combit_ele = self.wait_clickable_element((By.XPATH, '//span[text()="确认"]'))
            combit_ele.click()
         # 编辑
            edit_ele = self.wait_clickable_element((By.XPATH, '//span[@class="search-btn marginRight0"]'))
            edit_ele.click()
            Drag_01 = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[2]/div/div'))  # 找到滚动条
            #  控制滚动条的行为，每次向y轴(及向下)移动340个单位

            ActionChains(self.driver).drag_and_drop_by_offset(Drag_01, 0, 500).perform()
            # 循环定位三法
            for j in list_03:
                rule_ele = self.wait_clickable_element((By.XPATH, j))
                rule_ele.click()

            # 最终评估方法
            method_ele = self.wait_clickable_element((
                By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/input'))
            method_ele.click()
            method_ele_01 = self.wait_clickable_element((By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]'))
            method_ele_01.click()
            # 确定值
            self.multiple_send(list_04)
            #被评估单位所在地
            location = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[2]/div/div[3]/div/div/div/label[2]/span[1]/span'))
            location.click()
            location_01 = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/form/div[3]/div[2]/div[2]/div/div[4]/div/div/div/input'))
            location_01.click()
            location_01.send_keys("旧金山")
            save_ele = self.wait_clickable_element((By.XPATH, '//span[text()="保存"]'))
            save_ele.click()
            time.sleep(2)

# 下级单位编辑
        for j in list_02:
            # 选择单位
            company_ele = self.wait_clickable_element((By.XPATH, j))
            time.sleep(2)
            company_ele.click()
            time.sleep(3)
            try:
                rule_el = self.wait_clickable_element((By.XPATH, '//span[text()="+ 请选择作价模板"]'))
                rule_el.click()
                rule_el_01 = self.wait_clickable_element((By.XPATH, '//div[@class="template-con fs13"]'))
                rule_el_01.click()
                combit_ele = self.wait_clickable_element((By.XPATH, '//span[text()="确认"]'))
                combit_ele.click()
            except:
            # 编辑
                edit_ele = self.wait_clickable_element((
                    By.XPATH, '//span[@class="search-btn marginRight0"]'))
                edit_ele.click()
                # 循环定位三法
                for l in list_06:
                    rule_ele = self.wait_clickable_element((By.XPATH, l))
                    time.sleep(1)
                    rule_ele.click()

                # 最终评估方法
                method_ele_02 = self.wait_clickable_element((
                    By.XPATH,'//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/input'))
                method_ele_02.click()
                method_ele_03 = self.wait_clickable_element((By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]'))
                method_ele_03.click()
                # 确定值
                self.multiple_send(list_05)
                # 被评估单位所在地
                location_02 = self.wait_clickable_element((
                    By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[3]/div/div/div/label[2]/span[2]'))
                location_02.click()
                location_03 = self.wait_clickable_element((
                    By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div/form/div/div[2]/div[2]/div/div[4]/div/div/div/input'))
                location_03.click()
                location_03.send_keys("旧金山")
                save_ele_01 = self.wait_clickable_element((By.XPATH, '//span[text()="保存"]'))
                save_ele_01.click()
                time.sleep(2)
            

if __name__ == '__main__':
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("18611815532", "222222", "1111")
    project_name = ReadCong().read_conf()
    IndexPage(driver).search()
    Company(driver).edit_company()
