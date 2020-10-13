# _*_coding: utf-8 _*_
# @Time     :2020/1/18  17:59
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :project_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from mgy.pages.common.base import BasePage
'''xx项目页面
项目编辑，项目批量送审，项目编辑，单位编辑，变更提交 管理-报告盖章， 添加子公司，设为衍生，单位删除，立项撤回，立项审核通过'''


class ProjectPage(BasePage):

    # 项目（单位）编辑
    def edit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//span[text()="编辑"]'))
        return element_ele

    # 项目特征
    def characteristics(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.ID, '//div[@id="tab-first"]'))
        return element_ele

    # 其他信息
    def information(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.ID, '//div[@id="tab-contract"]'))
        return element_ele

    # 独立性自查
    def independent(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.ID, '//div[@id="tab-second"]'))
        return element_ele

    # 返回按钮
    def back(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//div[@class="backHome reset-btn marginLeft5 fr"]'))
        return element_ele

    # 立项提交
    def submit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//span[@class="submit search-btn"]'))
        return element_ele

    # 立项撤销
    def submit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//span[@class="revoke btn  search-btn"]'))
        return element_ele

    # 管理
    def administration(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//span[text()="管理"]'))
        return element_ele

    # 报告盖章
    def stamped(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[text()="报告盖章"]'))
        return element_ele

    # 批量编辑
    def batch_edit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[text()="批量编辑"]'))
        return element_ele

    # 批量送审
    def batch_submit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[text()="批量送审"]'))
        return element_ele

    # 开启内审
    def open_internal_audit(self):
        element_ele = self.wait_clickable_element((By.XPATH, '//span[text()="开启内审"]'))
        return element_ele

    # 取消内审
    def cancel_internal_audit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//span[text()="取消内审"]'))
        return element_ele

    # 意见反馈
    def opinions(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[@title="意见反馈"]'))
        return element_ele

    # 开启外审
    def open_external_audit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[text()="开启外审"]'))
        return element_ele

    # 关闭外审
    def close_external_audit(self) -> WebElement:
        element_ele = self.wait_clickable_element((By.XPATH, '//a[text()="关闭外审"]'))
        return element_ele