# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Project Endpoints
    'LIST_PROJECTS': 'projects/',
    'PROJECT': 'projects/%(project_name)s',
    'PROJECT_DESCRIPTION': 'projects/%(project_name)s/description',
    'PROJECT_PARENT': 'projects/%(project_name)s/parent',
    'HEAD': 'projects/%(project_name)s/HEAD',
    'REPOSITORY_STATISTICS': 'projects/%(project_name)s/statistics.git',
    'PROJECT_CONFIG': 'projects/%(project_name)s/config',
    'RUN_GC': 'projects/%(project_name)s/gc',
    'BAN_COMMIT': 'projects/%(project_name)s/ban',
    # Branch Endpoints
    'LIST_BRANCHES': 'projects/%(project_name)s/branches/',
    'BRANCH': 'projects/%(project_name)s/branches/%(branch_id)s/',
    'DELETE_BRANCHES': 'projects/%(project_name)s/branches:delete',
    'BRANCH_CONTENT': 'projects/%(project_name)s/branches/%(branch_id)s/files/%(file_id)s/content',
    'REFLOG': 'projects/%(project_name)s/branches/%(branch_id)s/reflog',
    # Child Project Endpoints
    'LIST_CHILD_PROJECTS': 'projects/%(project_name)s/children/',
    'CHILD_PROJECT': 'projects/%(project_name)s/children/%(child_project)s',
    # Tag Endpoints
    'LIST_TAGS': 'projects/%(project_name)s/tags/',
    'GET_TAG': 'projects/%(project_name)s/tags/%(tag)s',
    # Commit Endpoints
    'GET_COMMIT': 'projects/%(project_name)s/commits/%(commit_id)s',
    'COMMIT_CONTENT': 'projects/%(project_name)s/commits/%(commit_id)s/files/%(file_id)s/content',
    # Dashboard Endpoints
    'LIST_DASHBOARD': 'projects/%(project_name)s/dashboards/',
    'DASHBOARD': 'projects/%(project_name)s/dashboards/%(dashboard_id)s'
}


class Projects(object):
    """ This class provide projects-related methods
    Projects related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-projects.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list_projects(self):
        """Lists the projects accessible by the caller. """
        url = self.gerrit.url('LIST_PROJECTS')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_project(self, project):
        """Retrieves a project."""
        url = self.gerrit.url('PROJECT', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def create_project(self, project):
        """Creates a new project."""
        url = self.gerrit.url('PROJECT', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'name': name})
        return self.gerrit.dispatch(r)
