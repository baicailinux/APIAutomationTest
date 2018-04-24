# -*- coding:utf8 -*-
import ConfigParser
import pytest
from base.demoProject.demoProjectHttpClient import DemoProjectHttpClient
from common.strTool import getStringWithLBRB
"""
@pytest.fixture(scope='session')
其中scope可以有：
session：在整个测试session里只执行一次
module：在一个模块里只执行一次
class：在测试类里只执行一次
function：每个测试方法执行一次
"""

def getConfigInfo(section,name):
    config = ConfigParser.ConfigParser()
    config.read('config/config.ini')
    value=config.get(section,name)
    return value

@pytest.fixture(scope='session')
def demoProjectHttpClient():
    url =getConfigInfo('demoProject','url')
    demoProjectHttpClient=DemoProjectHttpClient(url,'utf-8')
    #测试接口如果都需要先授权，可以在再次操作，将授权信息放到httpclient的headers或者cookies
    httpResponseResult=demoProjectHttpClient.get('/horizon/auth/login/?next=/horizon/')
    cookies=httpResponseResult.cookies
    csrftoken=getStringWithLBRB(cookies,'csrftoken=',' for')
    demoProjectHttpClient.csrftoken=csrftoken
    #demoProjectHttpClient.setProxies({'http':'192.168.62.141:8888','https':'192.168.62.141:8888'})
    return demoProjectHttpClient