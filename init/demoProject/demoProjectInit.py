#-*- coding:utf8 -*-
from pojo.demoProjectConfig import DemoProjectConfig
import ConfigParser

class DemoProjectInit():
    def __init__(self):
        self._demoProjectConfig=self._readConfig('config/demoProjectInit.ini')


    def getDemoProjectConfig(self):
        return self._demoProjectConfig

    def _readConfig(self,configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile)
        demoProjectConfig=DemoProjectConfig()
        demoProjectConfig.url=config.get('servers','url')
        demoProjectConfig.adminUser=config.get('users','adminUser')
        demoProjectConfig.adminUserPassword = config.get('users', 'adminUserPassword')
        demoProjectConfig.normalUser=config.get('users','normalUser')
        demoProjectConfig.normalUserPassword=config.get('users','normalUserPassword')
        demoProjectConfig.closeUser=config.get('users','closeUser')
        demoProjectConfig.closeUserPassword=config.get('users','closeUserPassword')
        return demoProjectConfig

    def init(self):
        #每次测试前先清除上次构造的数据
        self._deinit()
        #初始化必要的数据，如在数据库中构建多种类型的账号，
        pass

    def _deinit(self):
        #清楚构造的数据
        pass
