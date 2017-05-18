# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    'SEARCH_DOCUMENTATION': 'Documentation/',
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
        url = self.gerrit.url('SEARCH_DOCUMENTATION')
        r = Request(
            method='GET',
            url=url,
            auth=self.gerrit.auth,
            params={'q': keyword})
        print r.url
        return self.gerrit.dispatch(r)
