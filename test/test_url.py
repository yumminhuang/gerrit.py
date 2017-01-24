from nose.tools import *

from gerrit.gerrit import Gerrit
from gerrit.config import Config


class test_url:
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_config_endpoints(self):
        gerrit_server = Gerrit('gerrit.example.com')
        config = Config(gerrit_server)
        assert_equal(
            config.gerrit.url('VERSION'),
            'http://gerrit.example.com/a/config/server/version')
