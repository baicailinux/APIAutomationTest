# -*- coding:utf8 -*-
import ConfigParser
import pytest
from base.demoProject.demoProjectClient import DemoProjectClient
from common.strTool import getStringWithLBRB
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
    #测试接口如果都需要先授权，可以在再次操作，将授权信息放到httpclient的headers或者cookies
    httpResponseResult=demoProjectClient.doRequest.get('/horizon/auth/login/?next=/horizon/')
    cookies=httpResponseResult.cookies
    csrftoken=getStringWithLBRB(cookies,'csrftoken=',' for')
    demoProjectClient.csrftoken=csrftoken
    #demoProjectHttpClient.setProxies({'http':'192.168.62.141:8888','https':'192.168.62.141:8888'})
    return demoProjectClient

# @pytest.fixture(scope='session')
# def voiceVerifyHttpClient():
#     url =getConfigInfo('voiceVerify','url')
#     voiceVerifyHttpClient=VoiceHttpClient(url,'utf-8')
#     return voiceVerifyHttpClient