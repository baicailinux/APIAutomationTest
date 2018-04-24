# -*- coding:utf8 -*-
from common.httpclient.doRequest import DoRequest

class DemoProjectHttpClient(DoRequest):
    def __init__(self,url,encoding='utf-8'):
        self._url=url
        self._encoding=encoding
        super(DemoProjectHttpClient,self).__init__(self._url,self._encoding)

        self._csrftoken=None

    @property
    def csrftoken(self):
        return self._csrftoken

    @csrftoken.setter
    def csrftoken(self,csrftoken):
        self._csrftoken=csrftoken