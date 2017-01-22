# -*- coding: utf-8 -*-

URLS = {
}


class Plugins(object):
    """ This class provide plugin-related methods
    Plugin related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-plugin.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
