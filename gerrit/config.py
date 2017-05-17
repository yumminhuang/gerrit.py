# -*- coding: utf-8 -*-

import json

from requests import Request

URLS = {
    'VERSION': 'config/server/version',
    'CACHES': 'a/config/server/caches',
    'CACHE': 'a/config/server/caches/%(cache)s',
    'FLUSH_CACHE': 'a/config/server/caches/%(cache)s/flush',
    'SUMMARY': 'a/config/server/summary?%(option)s',
    'CAPABILITIES': 'a/config/server/capabilities',
    'TASKS': 'a/config/server/tasks',
    'TASK': 'a/config/server/tasks/%(task_id)s',
}


class Config(object):
    """ This class provide config-related methods
    Config related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-config.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def get_version(self):
        """Returns the version of the Gerrit server.
        """
        url = self.gerrit.url('VERSION')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_caches(self):
        """Lists the caches of the server.
        Caches defined by plugins are included."""
        url = self.gerrit.url('CACHES')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def flush_caches(self, *caches):
        """Flush all caches
        """
        url = self.gerrit.url('CACHES')
        if cache:
            request_body = json.dumps({"operation": "FLUSH", "caches": caches})
        else:
            request_body = json.dumps({"operation": "FLUSH_ALL"})
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=request_body)
        return self.gerrit.dispatch(r)

    def flush_cache(self, cache):
        """Flushes a cache.
        """
        url = self.gerrit.url('FLUSH_CACHE', cache=cache)
        r = Request(method='POST', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_cache(self, cache):
        """Retrieves information about a cache.
        """
        url = self.gerrit.url('CACHE', cache=cache)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_summary(self, option):
        """Retrieves a summary of the current server state.
        """
        if option not in ['jvm', 'gc']:
            # TODO: define Exception?
            return (False, "option Not Allowed")
        url = self.gerrit.url('SUMMARY', option=option)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_capabilities(self):
        """Lists the capabilities that are available in the system."""
        url = self.gerrit.url('CAPABILITIES')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_tasks(self):
        """Lists the tasks from the background work queues that the Gerrit
        daemon is currently performing, or will perform in the near future."""
        url = self.gerrit.url('TASKS')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_task(self, task_id):
        """Retrieves a task from the background work queue that the Gerrit
        daemon is currently performing, or will perform in the near future."""
        url = self.gerrit.url('TASK', task_id=task_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def delete_task(self, task_id):
        """Kills a task from the background work queue that the Gerrit
        daemon is currently performing, or will perform in the near future."""
        url = self.gerrit.url('TASK', task_id=task_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
