# _*_coding: utf-8 _*_
# @Time     :2020/1/17  19:41
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :edit_project.py
'''项目编辑-立项提交-创建衍生项目'''
from mgy.pages.common.base import BasePage
from mgy.pages.common.project_page import ProjectPage
import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By


class EditProject(BasePage):
    # 项目名称输入框
    get_project_abbreviation_locator = '//input[@placeholder="请输入项目简称"]'
    # 点击项目性质
    click_project_nature_locator = '//input[@placeholder="请选择项目性质"]'
    # 点击项目级别
    click_project_level_locator = '//input[@placeholder="请选择项目级别"]'
    # 点击评估对象类型
    click_assessment_type_locator = '//div[@class="el-select select marginRight el-select--mini"]//input[@placeholder="请选择评估对象类型"] '
    click_assessment_type_01_locator = '//div[@class="el-select select el-select--mini"]//input[@placeholder="请选择评估对象类型"]'
    # 评估目的描述
    click_purpose_evaluation_locator = '//textarea[@placeholder="请输入评估目的描述"]'
    # 点击具体经济行为
    click_economic_behavior_locator = '//input[@placeholder="请选择具体经济行为"]'
    # 选择具体经济行为
    chose_economic_behavior_locator = '//li[@class="el-select-dropdown__item selected"]//span[text()="财务报告目的"]'
    # 点击价值类型
    click_value_type_locator = '//input[@placeholder="请选择价值类型"]'
    # 选择价值类型
    chose_value_type_locator = '//span[text()="市场价值"]'
    # 项目联络人
    project_contact_person_locator = "//input[@placeholder='请选择项目联络人']"
    # 添加联络人
    add_contact_person_locator = '//*[@id="pane-first"]/div/div[1]/div/div/div[3]/div[2]/div[2]/div/form/div[1]/div/div[1]/input'
    # 所属行业
    industry_locator = '//*[@id="pane-first"]/div/div[1]/div/div/div[1]/div[2]/form/div[21]/div/div/div/input'
    # 总资产账面值
    total_assets_locator = '//input[@placeholder="请输入总资产账面值"]'
    # 委托方名称
    get_entrusting_party_locator = '//*[@id="pane-contract"]/div/div[1]/div/div/form/div[1]/div[2]/ul/div/li[1]/div/div/div[1]/input'
    # 点击经济性质
    click_economic_nature_locator = '//div[@class="add-client"]//input[@placeholder="请选择经济性质"]'
    # 选择经济性质
    chose_economic_nature_locator = '/html/body/div[9]/div[1]/div[1]/ul/li[2]/span'
    # 创建衍生项目
    creat_derivative_items_locator = '//*[@id="app"]/div[2]/div[3]/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr[2]/td[2]/div/div/span[2]'

    # 点击项目编辑按钮
    def click_editor_project(self):
        click_editor_project_ele = ProjectPage(self.driver).edit()
        click_editor_project_ele.click()

    # 定位项目简称输入框
    def get_project_abbreviation(self):
        return self.wait_clickable_element((By.XPATH, self.get_project_abbreviation_locator))

    # 点击请选择项目性质
    def click_project_nature(self):
        click_project_nature_ele = self.wait_clickable_element((By.XPATH, self.click_project_nature_locator))
        click_project_nature_ele.click()

    # 选择项目性质 '//span[text()="通用项目"]' 涉军项目，房地产项目 矿权项目 土地项目，研究课题项目
    def chose_project_nature(self, locator):
        chose_project_nature_ele = self.wait_clickable_element((By.XPATH, locator))
        chose_project_nature_ele.click()

    # 点击选择项目级别
    def click_project_level(self):
        click_project_level_ele = self.wait_clickable_element((By.XPATH, self.click_project_level_locator))
        click_project_level_ele.click()

    # 选择项目级别  '//span[text()="A"]'
    def chose_project_level(self, locator):
        project_level_ele = self.wait_clickable_element((By.XPATH, locator))
        project_level_ele.click()

    # 点击请选择评估对象类型
    def click_assessment_type(self):
        assessment_type_ele = self.wait_clickable_element((By.XPATH, self.click_assessment_type_locator))
        assessment_type_ele.click()

    # 选择评估对象类型  '//span[text()="企业价值"]'
    def chose_assessment_type(self,locator):
        chose_assessment_type_ele = self.wait_clickable_element((By.XPATH, locator))
        chose_assessment_type_ele.click()

    # 点击请选择评估对象类型_01
    def click_assessment_type_01(self):
        assessment_type_ele_01 = self.wait_clickable_element((By.XPATH, self.click_assessment_type_01_locator))
        assessment_type_ele_01.click()

    # 点击请选择评估对象类型_01 '//span[text()="股东全部权益价值"]'
    def chose_assessment_type_01(self, locator):
        chose_assessment_type_ele_01 = self.wait_clickable_element((By.XPATH, locator))
        chose_assessment_type_ele_01.click()

    # 请输入评估目的描述
    def purpose_evaluation(self):
        description = self.wait_clickable_element((By.XPATH, self.click_purpose_evaluation_locator))
        description.send_keys('对公司企业进行价值评估')

    # 请选择具体经济行为
    def economic_behavior(self):
        behavior_ele = self.wait_clickable_element((By.XPATH, self.click_economic_behavior_locator))
        behavior_ele.click()
        chose_behavior_ele = self.wait_clickable_element((By.XPATH, self.chose_economic_behavior_locator))
        chose_behavior_ele.click()

    # 请选择价值类型
    def chose_value_type(self):
        click_value_type_ele = self.wait_clickable_element((By.XPATH, self.click_value_type_locator))
        click_value_type_ele.click()
        chose_value_type_ele = self.wait_clickable_element((By.XPATH, self.chose_value_type_locator))
        chose_value_type_ele.click()

    # 请选择项目联络人
    def project_contact_person(self):
        contact_person_ele = self.wait_clickable_element((By.XPATH, self.project_contact_person_locator))
        contact_person_ele.click()
        add_contact_person_ele = self.wait_clickable_element((By.XPATH, self.add_contact_person_locator))
        add_contact_person_ele.click()
        name = self.wait_clickable_element((By.XPATH, '//span[text()= "金阳"]'))
        name.click()
        firs_click = self.wait_clickable_element((By.XPATH, '//a[text()="确定"]'))
        firs_click.click()
        sen_click = self.wait_clickable_element((By.XPATH, '//a[text()="确认"]'))
        sen_click.click()

    # 所属行业
    def industry(self):
        click_industry_type = self.wait_clickable_element((By.XPATH, self.industry_locator))
        click_industry_type.click()
        chose_industry_type = self.wait_clickable_element((By.XPATH, '//span[text()="林业"]'))
        chose_industry_type.click()

    # 请输入总资产账面值
    def total_assets(self):
        return self.wait_clickable_element((By.XPATH, self.total_assets_locator))

    # 请选择现场工作时间
    def working_hours(self):
        working_hours_ele = self.wait_clickable_element((By.XPATH, '//input[@placeholder="请选择现场工作时间"]'))
        working_hours_ele.send_keys(30)

    # 控制滚动条
    def control_scroll_bar(self):
        drag = self.wait_clickable_element((By.XPATH, '//*[@id="pane-first"]/div/div[3]/div'))  # 找到滚动条
    #  控制滚动条的行为，每次向y轴(及向下)移动10个单位
        ActionChains(self.driver).drag_and_drop_by_offset(drag, 0, 500).perform()
        time.sleep(2)  # 休眠2秒

    # 项目特点
    def project_characteristics(self):
        for i in range(1, 16):
            locator = '//*[@id="pane-first"]/div/div[1]/div/div/div[2]/div[2]/form/div[{}]/div/div/label[2]' \
                      '/span[1]/span'.format(i)
            futures = self.wait_clickable_element((By.XPATH, locator))
            futures.click()

    # 其他信息  //div[text()="其他信息"]
    def click_other_information(self):
        other_information_ele = self.wait_clickable_element((By.XPATH, '//div[text()="其他信息"]'))
        other_information_ele.click()
        approved_department_ele = self.wait_clickable_element((By.XPATH, '//input[@placeholder="请输入核准、备案部门"]'))
        approved_department_ele.send_keys("北京")

    # 委托方名称
    def get_entrusting_party(self):
        click_entrusting_party_ele = self.wait_clickable_element((By.XPATH, self.get_entrusting_party_locator))
        click_entrusting_party_ele.send_keys("国家电网")
        entrusting_party_ele = self.wait_clickable_element((By.XPATH, '//span[text()="国外"]'))
        entrusting_party_ele.click()
        location_ele = self.wait_clickable_element((By.XPATH, '//input[@placeholder="请输入详细地址"]'))
        location_ele.send_keys("旧金山")
    # 找到滚动条
        drag_01 = self.wait_clickable_element((By.XPATH, '//*[@id="pane-contract"]/div/div[3]/div'))  # 找到滚动条
    #  控制滚动条的行为，每次向y轴(及向下)移动10个单位
        ActionChains(self.driver).drag_and_drop_by_offset(drag_01, 0, 250).perform()

    # 请选择经济性质
    def click_economic_nature(self):
        click_economic_nature_ele = self.wait_clickable_element((By.XPATH, self.click_economic_nature_locator))
        click_economic_nature_ele.click()
        chose_economic_nature_ele = self.wait_clickable_element((By.XPATH, self.chose_economic_nature_locator))
        chose_economic_nature_ele.click()

    # 请输入评估对象
    def other_matters(self):
        object_assessment_ele = self.wait_clickable_element((By.XPATH, '//input[@placeholder="请输入评估对象"]'))
        object_assessment_ele.send_keys("国家电网")

        # 请输入评估范围
        assessment_scope_ele = self.wait_clickable_element((By.XPATH, '//textarea[@placeholder="请输入评估范围"]'))
        assessment_scope_ele.send_keys("单位所有资产")

        # 请输入项目背景
        project_background_ele = self.wait_clickable_element((By.XPATH, '//textarea[@placeholder="请输入项目背景"]'))
        project_background_ele.send_keys("国企改革")

    # 独立性自查
    def independent_inspection(self):
        independent = self.wait_clickable_element((
            By.XPATH, '//div[text() = "独立性自查"]'))
        independent.click()
        inspection_01 = self.wait_clickable_element(
            (By.XPATH, '//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/label[1]/span[1]/span'))
        inspection_01.click()
        inspection_02 = self.wait_clickable_element(
            (By.XPATH, '//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/label[1]/span[1]/span'))
        inspection_02.click()
        inspection_03 = self.wait_clickable_element(
            (By.XPATH, '//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[3]/div/label[1]/span[1]/span'))
        inspection_03.click()

        # 保存 //span[text()="保存"]
    def click_preservation(self):
        preservation_ele = self.wait_clickable_element((By.XPATH, '//span[text()="保存"]'))
        preservation_ele.click()
        determine_ele = self.wait_clickable_element((By.XPATH, '//div[text()="确定"]'))
        determine_ele.click()

    #   创建衍生项目
    def creat_derivative_items(self):
        # 批量编辑
        batch_edit_ele = ProjectPage(self.driver).batch_edit()
        batch_edit_ele.click()
        creat_derivative_items_ele = self.wait_clickable_element((By.XPATH, self.creat_derivative_items_locator))
        creat_derivative_items_ele.click()
        drag_02 = self.wait_clickable_element((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div[2]/div/div'))  # 找到滚动条
        #  控制滚动条的行为，每次向y轴(及向下)移动10个单位
        ActionChains(self.driver).drag_and_drop_by_offset(drag_02, 0, 20).perform()
        save_ele = self.wait_clickable_element((By.XPATH, '//span[text()="保存"]'))
        save_ele.click()
        confirm_ele = self.wait_clickable_element((By.XPATH, '//button[text() = "确认"]'))
        confirm_ele.click()
        project_submission_ele = self.wait_clickable_element((By.XPATH, "//span[text()='立项提交']"))
        project_submission_ele.click()
        confirm_submission_ele = self.wait_clickable_element((By.XPATH, "//div[text()='确认提交']"))
        confirm_submission_ele.click()
        return_ele = self.wait_clickable_element((By.XPATH, '// div[text() = "返回"]'))
        return_ele.click()



