# -*- coding:utf8 -*-
from init.demoProject.demoProjectInit import DemoProjectInit
from common.httpclient.doRequest import DoRequest

class DemoProjectClient():
    def __init__(self):
        self.demoProjectConfig=DemoProjectInit().getDemoProjectConfig()
        self.doRequest=DoRequest(self.demoProjectConfig.url)
        self._csrftoken=None

    @property
    def csrftoken(self):
        return self._csrftoken

    @csrftoken.setter
    def csrftoken(self,csrftoken):
        self._csrftoken=csrftoken