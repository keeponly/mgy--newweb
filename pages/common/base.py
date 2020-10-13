# _*_coding: utf-8 _*_
# @Time     :2020/1/16  16:52
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :base.py
import time
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
# 用箭头确定会返回什么类型的数值，返回页面元素,locator是元组
'''EC.presence_of_element_located元素存在，但有可能隐藏'''
'''EC.visibility_of_element_located还必须检查元素是否存在以及元素是否可见'''
'''EC.element_to_be_clickable 元素可点击'''


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_visibility_element(self, locator, timeout=40, poll_frequency=0.1) -> WebElement:
        """等待元素出现 定义复杂，调用简单。"""
        try:
            user_ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
            return user_ele

        except Exception as e:
            # logger
            logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test0.jpg')

    def wait_find_element(self, locator, timeout=40, poll_frequency=0.1) ->WebElement:
        """等待元素出现 定义复杂，调用简单。"""
        try:
            user_ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator))
            return user_ele

        except Exception as e:
            # logger
            logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test.jpg')

    def wait_clickable_element(self, locator) -> WebElement:
        try:
            input_ele = WebDriverWait(self.driver, 40, 1).until(EC.element_to_be_clickable(locator))
            time.sleep(3)
            return input_ele
        except Exception as e:
            # logger
            logging.error('元素定位失败')
            # 截屏
            self.driver.save_screenshot('test1.jpg')

# 多重循环点击发送
    def multiple_send(self, list_value):
        for i in list_value:
            ele_value = self.wait_clickable_element((By.XPATH, i))
            ele_value.click()
            ele_value.send_keys('10')

    # 多重循环点击
    def multiple_click(self, list_value):
        for i in list_value:
            ele_value = self.wait_clickable_element((By.XPATH, i))
            time.sleep(1)
            ele_value.click()

    # 点击发送
    def click_send(self, ele_name, value):
        ele = self.wait_clickable_element((By.XPATH, ele_name))
        ele.click()
        ele.send_keys(value)

    # 上传文件
    def push(self):
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        # 找到窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 二级
        # 操作
        time.sleep(2)
        import win32con
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r'D:\work\cesuan.xlsx')  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        time.sleep(10)

