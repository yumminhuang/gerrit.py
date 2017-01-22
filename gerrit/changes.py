# -*- coding: utf-8 -*-

URLS = {
}


class Changes(object):
    """ This class provide change-related methods
    Change related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
