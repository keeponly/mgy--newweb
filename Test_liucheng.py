# _*_coding: utf-8 _*_
# @Time     :2020/1/9  11:18
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :Test_liucheng.py
import time
import win32con
import win32gui
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ActionChains
from pages.common.base import BasePage
from pages.common.read_conf import ReadCong
from pages.common.zlpg_home import IndexPage
from pages.page.login import LoginPage
import win32gui
import win32con


# 主页项目搜索
class PushFile(BasePage):
    def push_file(self, locat):
        company = self.wait_clickable_element((By.XPATH, locat))
        company.click()
        shangchuan_01 = self.wait_clickable_element((By.XPATH, "//span[text()='附件模式']"))
        shangchuan_01.click()
        shangchuan_02 = self.wait_clickable_element((By.XPATH, '//a[text()="上传文件"]'))
        shangchuan_02.click()
        shangchuan_03 = self.wait_clickable_element((By.XPATH, '//a[text()="+ 添加"]'))
        shangchuan_03.click()
        time.sleep(2)
        # 找到对应的窗口
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        # 找到窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 二级
        # 操作
        time.sleep(2)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r'D:\work\cesuan.xlsx')  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        time.sleep(2)


if __name__ == '__main__':
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("18611815532", "222222", "1111")
    time.sleep(3)
    # 搜索项目
    locat = '//*[@id="app"]/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]/span[2]/span'
    project_name = ReadCong().read_conf()
    IndexPage(driver).search(project_name)
    # 上传
    PushFile(driver).push_file(locat)
