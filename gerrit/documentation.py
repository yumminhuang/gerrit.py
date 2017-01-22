# -*- coding: utf-8 -*-

URLS = {
}


class Documentation(object):
    """ This class provide documentation-related methods
    Documentation related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-documentation.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
