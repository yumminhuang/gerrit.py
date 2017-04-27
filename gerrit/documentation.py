# -*- coding: utf-8 -*-

from requests import Request
from urllib import quote

URLS = {
    'SEARCH_DOCUMENTATION': 'Documentation/?q=%(keyword)s',
}


class Documentation(object):
    """ This class provide documentation-related methods
    Documentation related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-documentation.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def search(self, keyword):
        """With q parameter, search our documentation index for the terms."""
        url = self.gerrit.url('SEARCH_DOCUMENTATION', keyword=quote(keyword))
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
