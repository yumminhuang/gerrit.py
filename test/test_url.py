# -*- coding: utf-8 -*-

from nose.tools import *
from requests import Request

from gerrit.access import Access
from gerrit.config import Config
from gerrit.documentation import Documentation
from gerrit.gerrit import Gerrit


class test_url:
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.gerrit_server = Gerrit('gerrit.example.com')

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_config_endpoints(self):
        config = Config(self.gerrit_server)
        assert_equal(
            config.gerrit.url('VERSION'),
            'http://gerrit.example.com/config/server/version')
        assert_equal(
            config.gerrit.url('CACHES'),
            'http://gerrit.example.com/a/config/server/caches')

    def test_documentation_endpoints(self):
        doc = Documentation(self.gerrit_server)
        assert_equal(
            doc.gerrit.url('SEARCH_DOCUMENTATION'),
            'http://gerrit.example.com/Documentation/')

    def test_access_endpoints(self):
        access = Access(self.gerrit_server)
        r = Request(
            method='GET',
            url=access.gerrit.url('LIST_ACCESS'),
            params={'project': 'All-Projects'})
        assert_equal(
            r.prepare().url,
            'http://gerrit.example.com/a/access/?project=All-Projects')
