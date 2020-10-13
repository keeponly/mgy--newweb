# _*_coding: utf-8 _*_
# @Time     :2020/2/11  12:26
# @Author   :wang-kai
# @tel      :15313929271
# @ File    :read_conf.py
import os
from configparser import ConfigParser
# 创建对象


class ReadCong():
    def read_conf(self):
        cf = ConfigParser()
        cf.read(r'D:\work\PycharmProjects\mgy\test_data/project.conf', encoding='utf-8')
        res = cf.get('project', 'project_01')
        return res