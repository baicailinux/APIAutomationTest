# -*- coding:utf8 -*-
import ConfigParser


class DemoProjectConfig():
    def __init__(self):
        self.url = None
        self.adminUser = None
        self.adminUserPassword = None
        self.normalUser = None
        self.normalUserPassword = None
        self.closeUser = None
        self.closeUserPassword = None

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, url):
        self.url = url

    @property
    def adminUser(self):
        return self.adminUser

    @adminUser.setter
    def adminUser(self, adminUser):
        self.adminUser = adminUser

    @property
    def adminUserPassword(self):
        return self.adminUserPassword

    @adminUserPassword.setter
    def adminUserPassword(self, adminUserPassword):
        self.adminUserPassword = adminUserPassword

    @property
    def normalUser(self):
        return self.normalUser

    @normalUser.setter
    def normalUser(self, normalUser):
        self.normalUser = normalUser

    @property
    def normalUserPassword(self):
        return self.normalUserPassword

    @normalUserPassword.setter
    def normalUserPassword(self, normalUserPassword):
        self.normalUserPassword = normalUserPassword

    @property
    def closeUser(self):
        return self.closeUser

    @closeUser.setter
    def closeUser(self, closeUser):
        self.closeUser = closeUser

    @property
    def closeUserPassword(self):
        return self.closeUserPassword

    @closeUserPassword.setter
    def closeUserPassword(self, closeUserPassword):
        self.closeUserPassword = closeUserPassword
