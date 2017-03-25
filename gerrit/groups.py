# -*- coding: utf-8 -*-

from requests import Request

URLS = {}


class Groups(object):
    """ This class provide groups-related methods
    Groups related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-groups.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
