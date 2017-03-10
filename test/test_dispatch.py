# -*- coding: utf-8 -*-
import json

from requests import Request
from nose.tools import *

from gerrit.gerrit import Gerrit

httpbin = 'http://httpbin.org/'


class test_url:
    def setUp(self):
        self.gerrit = Gerrit(httpbin, 'admin', 'password')

    def teardown(self):
        self.gerrit = None

    def test_default_credential(self):
        assert_equal(self.gerrit.username, 'admin')
        assert_equal(self.gerrit.password, 'password')
        assert_equal(self.gerrit.host, httpbin)
        assert_is_instance(self.gerrit.URLS, dict)

    def test_dispatch_get(self):
        success, result = self.gerrit.dispatch(
            Request(
                method='GET', url=httpbin + 'get'))
        assert_true(success)
        success, result = self.gerrit.dispatch(
            Request(
                method='GET', url=httpbin + 'get1'))
        assert_false(success)

    def test_dispatch_post(self):
        success, result = self.gerrit.dispatch(
            Request(
                method='POST', url=httpbin + 'post', data={'foo': 'bar'}))
        assert_true(success)
        success, result = self.gerrit.dispatch(
            Request(
                method='GET', url=httpbin + 'post', data={'foo': 'bar'}))
        assert_false(success)

    def test_dispatch_put(self):
        success, result = self.gerrit.dispatch(
            Request(
                method='PUT', url=httpbin + 'put', data={'foo': 'bar'}))
        assert_true(success)

    def test_dispatch_delete(self):
        success, result = self.gerrit.dispatch(
            Request(
                method='DELETE', url=httpbin + 'delete'))
        assert_true(success)
