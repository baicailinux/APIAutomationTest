# -*- coding:utf8 -*-
from init.demoProject.demoProjectInit import DemoProjectInit
from common.httpclient.doRequest import DoRequest
from common.strTool import StrTool

class DemoProjectClient():
    def __init__(self):
        self.demoProjectConfig=DemoProjectInit().getDemoProjectConfig()
        self.doRequest=DoRequest(self.demoProjectConfig.url)
        self.csrftoken=None

        self._initCsrftoken()

    def _initCsrftoken(self):
        # 测试接口如果都需要先授权，可以在再次操作，将授权信息放到httpclient的headers或者cookies
        httpResponseResult = self.doRequest.get("/horizon/auth/login/?next=/horizon/")
        cookies = httpResponseResult.cookies
        csrftoken = StrTool.getStringWithLBRB(cookies, 'csrftoken=', ' for')
        self.csrftoken = csrftoken