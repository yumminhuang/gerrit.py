# -*- coding: utf-8 -*-

import json

from requests import Session
from requests.auth import HTTPDigestAuth


class Gerrit(object):
    """ This class lets you interact with the Gerrit REST API. """

    def __init__(self, host='', username='', password=''):
        self.URLS = {
            'BASE': 'http://%s/%%s' % host,
        }
        self.host = host
        self.username = username
        self.password = password

    @property
    def host(self):
        """Return host."""
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

        if value is None:
            self._host = None

    @host.deleter
    def host(self):
        del self._host

    @property
    def username(self):
        """Return username."""
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

        if value is None:
            self._username = None

    @username.deleter
    def username(self):
        del self._username

    @property
    def password(self):
        """Return password."""
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

        if value is None:
            self._password = None

    @password.deleter
    def password(self):
        del self._password

    @property
    def auth(self):
        """ Return credentials for current user. """
        return HTTPDigestAuth(self.username, self.password)

    def url(self, action, **kwargs):
        """ Construct and return the URL for a specific API service. """
        return self.URLS['BASE'] % self.URLS[action] % kwargs

    def dispatch(self, request):
        """ Send HTTP request, and return the success
        and the result on success.
        """
        s = Session()
        resp = s.send(request.prepare())
        status = resp.status_code
        content = resp.content

        error = resp.reason
        if status >= 200 and status < 300:
            if content:
                try:
                    return (True, json.loads(content[5:]))
                except TypeError:
                    pass
                except ValueError:
                    pass

            return (True, content)
        elif status == 400:
            return (False, "Bad Request")
        elif status == 403:
            return (False,
                    "Forbidden: You may not have sufficient permissions")
        elif status == 404:
            return (False, "Service not found (%s to %s): %s " %
                    (request.method, request.url, content))
        elif status == 405:
            return (False, "Method Not Allowed")
        elif status == 409:
            return (False, "Conflict")
        elif status == 412:
            return (False, "Precondition Failed")
        elif status == 422:
            return (False, "Unprocessable Entity")
        elif status >= 500 and status < 600:
            return (False, 'Server error.')
        else:
            return (False, error)
