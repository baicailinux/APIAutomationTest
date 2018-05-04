# -*- coding:utf8 -*-
import pytest

from base.demoProject.demoProjectClient import DemoProjectClient
from common.strTool import StrTool
"""
@pytest.fixture(scope='session')
其中scope可以有：
session：在整个测试session里只执行一次
module：在一个模块里只执行一次
class：在测试类里只执行一次
function：每个测试方法执行一次
"""

@pytest.fixture(scope='session')
def demoProjectClient():
    demoProjectClient=DemoProjectClient()
    return demoProjectClient