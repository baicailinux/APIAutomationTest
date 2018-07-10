#-*- coding:utf8 -*-
from assertpy import assert_that
from base.demoProject.demoProjectClient import DemoProjectClient
import pytest

class TestLogin():

    def setup_class(self):
        self._demoProjectClient=DemoProjectClient()
        self._login_path='/horizon/auth/login/'

    @pytest.fixture
    def fixture_test_success_login_scenrario(self):
        #setup
        print 'this is a setup'
        #teardown
        yield self.fixture_test_success_login_scenrario
        print 'this is a teardown'

    def generateParams(self,csrfmiddlewaretoken,username,password,fake_email,fake_password):
        params={}
        params.update({"csrfmiddlewaretoken":csrfmiddlewaretoken})
        params.update({"username": username})
        params.update({"password": password})
        params.update({"fake_email": fake_email})
        params.update({"fake_password": fake_password})
        return params

    @pytest.mark.scenrario
    def test_success_login_scenrario(self,fixture_test_success_login_scenrario):
        params=self.generateParams(self._demoProjectClient.csrftoken,'admin','admin','admin','admin')
        httpResponseResult=self._demoProjectClient.doRequest.post_with_form(self._login_path,params=params)
        status_code=httpResponseResult.status_code
        body=httpResponseResult.body
        assert_that(status_code).is_equal_to(200)
        assert_that(body).contains('admin')
