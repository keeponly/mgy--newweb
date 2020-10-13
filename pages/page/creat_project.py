# _*_coding: utf-8 _*_
# @Time     :2020/1/16  21:38
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :creat_project.py
# 创建项目
"""
.在首页点击创建项目
.填写项目信息
.保存，创建项目
.断言，查看项目是否创建成功
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from mgy.pages.common.base import BasePage
from mgy.pages.common.zlpg_home import IndexPage

'''评估报告 估值报告 咨询报告 土地估价报告 矿权评估报告 矿权咨询报告 房地产估价报告'''


class CreatPage(BasePage):

    """创建项目页面"""

    # 项目名称输入框
    get_input_project_name_locator = "//input[@placeholder='请输入项目名称']"
    # 点击评估报告类型
    click_project_type_locator = "//input[@placeholder='请选择评估报告类型']"
    # 选择评估报告类型
    chose_project_type_locator = "//span[text()='评估报告']"
    # 点击评估基准日
    click_base_date_locator = "//input[@placeholder='选择评估基准日']"
    # 选择评估基准日
    chose_base_data_locator = "//span[text()=9]"
    # 点击评估目的
    click_purpose_evaluation_locator = "//input[@placeholder='请选择评估目的类型']"
    # 选择评估目的
    chose_purpose_evaluation_locator = "//span[text()='改建']"
    # 预期合同及
    except_price_locator = "//input[@placeholder='请输入预期合同价']"
    # 第一签字评估师
    first_signer_locator = "//input[@placeholder='请选择第一签字评估师']"
    # 第二签字评估师
    second_signer_locator = "//input[@placeholder='请选择第二签字评估师']"
    # 签字评估师名字
    first_signer_name_locator = '//span[text()="王大鹏"]'
    second_signer_name_locator = '//span[text()="金阳"]'
    # 确认签字评估师
    confirm_locator = '//a[@class="search-btn"]'
    # 股权树
    # 单位1名称输入框
    company_name_locator = '//input[@class="input frist-tr text-left"]'
    # 添加子公司按钮
    add_to_locator = "//span[text() = '添加子公司']"
    # 子公司名称输入框
    subsidiary_name_locator = "//*[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/div/input"
    # 子公司添加子公司
    add_to_locator_01 = "//*[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/div/span[1]"
    # 子公司子公司名称输入框
    subsidiary_name_01_locator = '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[3]/td[1]/div/input'
    # 同级公司添加按钮
    same_level_company_locator = "//span[text() = '添加同级公司']"
    # 同级公司名称输入框
    same_leve_company_name_locator = '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[4]/td[1]/div/input'
    # 同级公司下添加子公司按钮
    same_level_subsidiary_locator = '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[4]/td[2]/div/div/span[1]'
    # 子公司输入框
    same_level_subsidiary_name_locator = '//*[@id="app"]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[5]/td[1]/div/input'
    # 创建
    establish_locator = "//*[text()='创建']"
    # 确定
    confirm_locator_submission = '//div[@class="search-btn"]'

    # 点击创建项目按钮
    def creat_project(self):
        creat_project_element_ele = IndexPage(self.driver).creat_project()  # 定位创建项目按钮
        creat_project_element_ele.click()

    # 定位项目名称输入框
    def get_input_project_name(self):
        return self.wait_visibility_element((By.XPATH, self.get_input_project_name_locator))

    # 点击报告类型
    def click_project_type(self):
        report_type_ele = self.wait_clickable_element((By.XPATH, self.click_project_type_locator))
        report_type_ele.click()

    # 选择报告类型
    def chose_project_type(self, locator):
        chose_type_ele = self.wait_clickable_element((By.XPATH, locator))
        chose_type_ele.click()

    # 点击评估基准日
    def click_base_date(self):
        base_date_ele = self.wait_clickable_element((By.XPATH, self.click_base_date_locator))
        base_date_ele.click()
    # 选择评估基准日
        chose_base_data_ele = self.wait_clickable_element((By.XPATH, self.chose_base_data_locator))
        chose_base_data_ele.click()

    # 点击评估目的
    def click_purpose_evaluation(self):
        purpose_ele = self.wait_clickable_element((By.XPATH, self.click_purpose_evaluation_locator))
        purpose_ele.click()
    # 选择评估目的
        chose_purpose_ele = self.wait_clickable_element((By.XPATH, self.chose_purpose_evaluation_locator))
        chose_purpose_ele.click()

    # 预期合同价
    def get_except_price(self):
        return self.wait_clickable_element((By.XPATH, self.except_price_locator))

    # 第一评估师
    def first_signer(self):
        first_signer_ele = self.wait_clickable_element((By.XPATH, self.first_signer_locator))
        first_signer_ele.click()
    # 选择第一签字评估师
        first_signer_name_ele = self.wait_clickable_element((By.XPATH, self.first_signer_name_locator))
        first_signer_name_ele.click()
    # 确认第一签字评估师
        confirm_ele = self.wait_clickable_element((By.XPATH, self.confirm_locator))
        confirm_ele.click()

    # 第二评估师
    def second_signer(self):
        second_signer_ele = self.wait_clickable_element((By.XPATH, self.second_signer_locator))
        second_signer_ele .click()
    # 选择第二签字评估师
        second_signer_name_ele = self.wait_clickable_element((By.XPATH, self.second_signer_name_locator))
        second_signer_name_ele.click()
    # 确认第二签字评估师
        second_click = self.wait_clickable_element((By.XPATH, self.confirm_locator))
        second_click.click()

    # 股权信息树
    def equity_tree(self):
        company_name_01_ele = self.wait_clickable_element((By.XPATH, self.company_name_locator))
        company_name_01_ele.send_keys("第一公司")
        # "添加子公司"
        add_to_ele = self.wait_clickable_element((By.XPATH, self.add_to_locator))
        add_to_ele.click()
        # 子公司1名称
        subsidiary_name_ele = self.wait_clickable_element((By.XPATH, self.subsidiary_name_locator))
        subsidiary_name_ele.send_keys("附件1")
        # 子公司的子公司，添加子公司按钮
        add_to_ele_01 = self.wait_clickable_element((By.XPATH, self.add_to_locator_01))
        add_to_ele_01.click()
        # 子公司子公司名称
        subsidiary_name_ele_01 = self.wait_clickable_element((By.XPATH, self.subsidiary_name_01_locator))
        subsidiary_name_ele_01.send_keys("附件2")
        # 添加同级公司
        same_level_company_ele = self.wait_clickable_element((By.XPATH, self.same_level_company_locator))
        same_level_company_ele.click()
        # 同级公司名称
        same_level_company_name_ele = self.wait_clickable_element((By.XPATH, self.same_leve_company_name_locator))
        same_level_company_name_ele.send_keys("第二公司")
        # 同级下添加子公司按钮
        same_level_subsidiary_ele = self.wait_clickable_element((By.XPATH, self.same_level_subsidiary_locator))
        same_level_subsidiary_ele.click()
        # 公司名称输入框
        same_level_subsidiary_ele_name = self.wait_clickable_element((By.XPATH, self.same_level_subsidiary_name_locator))
        same_level_subsidiary_ele_name.send_keys("混合1")

    # 创建
    def establish(self):
        establish_ele = self.wait_clickable_element((By.XPATH, self.establish_locator))
        establish_ele.click()

    # 确认创建
    def confirm(self):
        confirm_ele = self.wait_clickable_element((By.XPATH, self.confirm_locator_submission ))
        confirm_ele.click()

        # 定位登录错误提示提醒
    def get_flash_info(self) -> WebElement:
        error_msg = self.wait_find_element((By.XPATH, '//p[text()="请输入必填项"]'))
        return error_msg








