# _*_coding: utf-8 _*_
# @Time     :2020/1/15  23:09
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :project_data.py
from selenium.webdriver import Chrome,Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from mgy.pages.common.base import BasePage


class LoginPage(BasePage):

    url = "https://oms-bate.cailian.net/#/login"

    def login(self, username, password, code):
        # 登录操作
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_ele = self.get_use_info()
        pwd_ele = self.get_pwd_info()
        verification_ele = self.get_verification_info()
        user_ele.send_keys(username)
        pwd_ele.send_keys(password)
        verification_ele.send_keys(code)
        submit_elc = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "submit-btn")))
        submit_elc.click()
        return self.driver

# 定位登录错误提示提醒
    def get_flash_info(self) -> WebElement:
        error_msg = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="el-form-item__error"]')))
        return error_msg

# 清空密码
    def clear_pwd_info(self):
        return self.get_pwd_info().clear()

# 清空账号
    def clear_verification_info(self):
        return self.get_verification_info().clear()

# 定位用户名输入框
    def get_use_info(self) -> WebElement:
        user_ele = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='请输入用户名']")))
        return user_ele

# 定位密码输入框
    def get_pwd_info(self) -> WebElement:
        user_ele = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='请输入密码']")))
        return user_ele

# 定位验证码输入框
    def get_verification_info(self) -> WebElement:
        verification_ele = WebDriverWait(self.driver, 40, 1).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='请输入验证码']")))
        return verification_ele


if __name__ == '__main__':
    driver = Firefox()
    LoginPage(driver).login("13611110000", "123456", "1111")
