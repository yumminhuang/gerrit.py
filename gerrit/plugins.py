# -*- coding: utf-8 -*-

URLS = {
    'LIST': 'plugins/',
    'INSTALL': 'plugins/%(plugin_id)s',
    'STATUS': 'plugins/%(plugin_id)s/gerrit~status',
    'ENABLE': 'plugins/%(plugin_id)s/gerrit~enable',
    'DISABLE': 'plugins/%(plugin_id)s/gerrit~disable',
    'RELOAD': 'plugins/%(plugin_id)s/gerrit~reload',
}


class Plugins(object):
    """ This class provide plugin-related methods
    Plugin related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-plugin.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list(self, list_all=False):
        """Lists the plugins installed on the Gerrit server.
        Only the enabled plugins are returned
        unless the all option is specified."""
        url = self.gerrit.url('LIST')
        if list_all:
            url += '?all'
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def install(self, plugin_id):
        """Installs a new plugin on the Gerrit server.
        """
        # TODO: install
        pass

    def status(self, plugin_id):
        """Retrieves the status of a plugin on the Gerrit server."""
        url = self.gerrit.url('STATUS', plugin_id=plugin_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def enable(self, plugin_id):
        """Enables a plugin on the Gerrit server."""
        url = self.gerrit.url('ENABLE', plugin_id=plugin_id)
        r = Request(method='POST', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def disable(self, plugin_id):
        """Disables a plugin on the Gerrit server."""
        url = self.gerrit.url('DISABLE', plugin_id=plugin_id)
        r = Request(method='POST', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def reload(self, plugin_id):
        """Reloads a plugin on the Gerrit server."""
        url = self.gerrit.url('RELOAD', plugin_id=plugin_id)
        r = Request(method='POST', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
