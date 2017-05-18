# -*- coding: utf-8 -*-

from requests import Request

URLS = {'LIST_ACCESS': 'a/access/'}


class Access(object):
    """ This class provide access-related methods
    Access related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-access.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list_access(self, *projects):
        """Lists the access rights for projects.
        """
        url = self.gerrit.url('LIST_ACCESS')
        r = Request(
            method='GET',
            url=url,
            auth=self.gerrit.auth,
            params={'project': projects})
        return self.gerrit.dispatch(r)
