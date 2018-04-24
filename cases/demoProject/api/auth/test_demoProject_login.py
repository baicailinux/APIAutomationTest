#-*- coding:utf8 -*-
from assertpy import assert_that
import pytest

class TestLogin():

    def setup_class(self):
        self._login_path='/horizon/auth/login/'

    def generateParams(self,csrfmiddlewaretoken,username,password,fake_email,fake_password):
        params={}
        params.update({"csrfmiddlewaretoken":csrfmiddlewaretoken})
        params.update({"username": username})
        params.update({"password": password})
        params.update({"fake_email": fake_email})
        params.update({"fake_password": fake_password})
        return params

    def test_success_login(self,demoProjectHttpClient):
        params=self.generateParams(demoProjectHttpClient.csrftoken,'admin','admin','admin','admin')
        httpResponseResult=demoProjectHttpClient.post_with_form(self._login_path,params=params)
        status_code=httpResponseResult.status_code
        body=httpResponseResult.body
        assert_that(status_code).is_equal_to(200)
        assert_that(body).contains('admin')

    def test_fail_login(self,demoProjectHttpClient):
        params=self.generateParams(demoProjectHttpClient.csrftoken,'admin','admin1','admin','admin1')
        httpResponseResult=demoProjectHttpClient.post_with_form(self._login_path,params=params)
        status_code=httpResponseResult.status_code
        body=httpResponseResult.body
        assert_that(status_code).is_equal_to(403)
        assert_that(body).contains('admin')

    @pytest.mark.skip(reason='空密码前端做校验')
    def test_empty_password_login(self,demoProjectHttpClient):
        params=self.generateParams(demoProjectHttpClient.csrftoken,'admin','','admin','')
        httpResponseResult=demoProjectHttpClient.post_with_form(self._login_path,params=params)
        status_code=httpResponseResult.status_code
        body=httpResponseResult.body
        assert_that(status_code).is_equal_to(403)
        assert_that(body).contains('admin')

    fail_data=[('11111','1111'),('admin',''),('',''),('中文用户名','中文密码')]
    @pytest.mark.parametrize('username,password',fail_data)
    def test_with_params_fail_login(self,username,password,demoProjectHttpClient):
        params = self.generateParams(demoProjectHttpClient.csrftoken, username, password, username, password)
        httpResponseResult = demoProjectHttpClient.post_with_form(self._login_path, params=params)
        status_code = httpResponseResult.status_code
        body=httpResponseResult.body
        assert_that(status_code).is_equal_to(403)
        assert_that(body).contains('admin')


    def teardown_class(self):
        pass

