# -*- coding:utf8 -*-
from common.httpclient.doRequest import DoRequest

class VoiceHttpClient(DoRequest):
    def __init__(self,url,encoding='utf-8'):
        self._url = url
        self._encoding = encoding
        super(VoiceHttpClient,self).__init__(self._url,self._encoding)