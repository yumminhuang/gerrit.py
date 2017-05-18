# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Project Endpoints
    'LIST_PROJECTS':
    'a/projects/',
    'PROJECT':
    'a/projects/%(project_name)s',
    'PROJECT_DESCRIPTION':
    'a/projects/%(project_name)s/description',
    'PROJECT_PARENT':
    'a/projects/%(project_name)s/parent',
    'HEAD':
    'a/projects/%(project_name)s/HEAD',
    'REPOSITORY_STATISTICS':
    'a/projects/%(project_name)s/statistics.git',
    'PROJECT_CONFIG':
    'a/projects/%(project_name)s/config',
    'RUN_GC':
    'a/projects/%(project_name)s/gc',
    'BAN_COMMIT':
    'a/projects/%(project_name)s/ban',
    # Branch Endpoints
    'LIST_BRANCHES':
    'a/projects/%(project_name)s/branches/',
    'BRANCH':
    'a/projects/%(project_name)s/branches/%(branch_id)s/',
    'DELETE_BRANCHES':
    'a/projects/%(project_name)s/branches:delete',
    'BRANCH_CONTENT':
    'a/projects/%(project_name)s/branches/%(branch_id)s/files/%(file_id)s/content',
    'REFLOG':
    'a/projects/%(project_name)s/branches/%(branch_id)s/reflog',
    # Child Project Endpoints
    'LIST_CHILD_PROJECTS':
    'a/projects/%(project_name)s/children/',
    'CHILD_PROJECT':
    'a/projects/%(project_name)s/children/%(child_project)s',
    # Tag Endpoints
    'LIST_TAGS':
    'a/projects/%(project_name)s/tags/',
    'GET_TAG':
    'a/projects/%(project_name)s/tags/%(tag)s',
    # Commit Endpoints
    'GET_COMMIT':
    'a/projects/%(project_name)s/commits/%(commit_id)s',
    'COMMIT_CONTENT':
    'a/projects/%(project_name)s/commits/%(commit_id)s/files/%(file_id)s/content',
    # Dashboard Endpoints
    'LIST_DASHBOARD':
    'a/projects/%(project_name)s/dashboards/',
    'DASHBOARD':
    'a/projects/%(project_name)s/dashboards/%(dashboard_id)s'
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

    def create_project(self, project, project_info):
        """Creates a new project."""
        url = self.gerrit.url('PROJECT', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=project_info)
        return self.gerrit.dispatch(r)

    def get_project_description(self, project):
        """Retrieves the description of a project."""
        url = self.gerrit.url('PROJECT_DESCRIPTION', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_project_description(self, project, project_description_info):
        """Sets the description of a project."""
        url = self.gerrit.url('PROJECT_DESCRIPTION', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=project_description_info)
        return self.gerrit.dispatch(r)

    def delete_project_description(self, project):
        """Deletes the description of a project."""
        url = self.gerrit.url('PROJECT_DESCRIPTION', project_name=project)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
