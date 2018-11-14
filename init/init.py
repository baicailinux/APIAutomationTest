# -*- coding:utf8 -*-
from demoProject.demoProjectInit import DemoProjectInit
import ConfigParser


def init():
    """
    初始化必要的数据
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('config/init.ini')

    # 初始化demoProject项目基础数据
    if 1 == int(config.get('isInit', 'demoProject')):
        DemoProjectInit().init()
