# -*- coding: utf-8 -*-

URLS = {
}


class Config(object):
    """ This class provide config-related methods
    Config related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-config.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
