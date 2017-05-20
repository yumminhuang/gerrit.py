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
    'LIST_DASHBOARDS':
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

    def get_project_parent(self, project):
        """Retrieves the name of a project’s parent project.
        For the All-Projects root project an empty string is returned."""
        url = self.gerrit.url('PROJECT_PARENT', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_project_parent(self, project, project_parent_info):
        """Sets the parent project for a project."""
        url = self.gerrit.url('PROJECT_PARENT', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=project_parent_info)
        return self.gerrit.dispatch(r)

    def get_project_parent(self, project):
        """Retrieves for a project the name of the branch to which HEAD points."""
        url = self.gerrit.url('HEAD', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_project_parent(self, project, ref):
        """Sets HEAD for a project."""
        url = self.gerrit.url('HEAD', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'ref': ref})
        return self.gerrit.dispatch(r)

    def get_repository_statistics(self, project):
        """Return statistics for the repository of a project."""
        url = self.gerrit.url('REPOSITORY_STATISTICS', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_project_config(self, project):
        """Gets some configuration information about a project. """
        url = self.gerrit.url('PROJECT_CONFIG', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_project_config(self, project, config_info):
        """Sets the configuration of a project."""
        url = self.gerrit.url('PROJECT_CONFIG', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=config_info)
        return self.gerrit.dispatch(r)

    def run_gc(self, project, show_progress=False):
        """Run the Git garbage collection for the repository of a project."""
        url = self.gerrit.url('RUN_GC', project_name=project)
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'show_progress': show_progress})
        return self.gerrit.dispatch(r)

    def ban_commits(self, project, ban_input_info):
        """Marks commits as banned for the project."""
        url = self.gerrit.url('BAN_COMMIT', project_name=project)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=ban_input_info)
        return self.gerrit.dispatch(r)

    def list_project_branches(self, project, **query):
        """List the branches of a project.
        Available parameters:
        n: limit number
        s: skip number
        m: query substring
        r: query Regex
        """
        url = self.gerrit.url('LIST_BRANCHES', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth, params=query)
        return self.gerrit.dispatch(r)

    def get_project_branch(self, project, branch):
        """Retrieves a branch of a project."""
        url = self.gerrit.url('BRANCH', project_name=project, branch_id=branch)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def create_project_branch(self, project, branch, revision):
        """Creates a new branch."""
        url = self.gerrit.url('BRANCH', project_name=project, branch_id=branch)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'revision': revision})
        return self.gerrit.dispatch(r)

    def delete_project_branch(self, project, branch):
        """Deletes a branch."""
        url = self.gerrit.url('BRANCH', project_name=project, branch_id=branch)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def delete_project_branches(self, project, branches):
        """Delete one or more branches."""
        url = self.gerrit.url('DELETE_BRANCHES', project_name=project)
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'branches': branches})
        return self.gerrit.dispatch(r)

    def get_branch_content(self, project, branch, file):
        """Gets the content of a file from the HEAD revision of a certain
        branch. The content is returned as base64 encoded string."""
        url = self.gerrit.url(
            'BRANCH_CONTENT',
            project_name=project,
            branch_id=branch,
            file_id=file)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_reflog(self, project, branch, *query):
        """Gets the reflog of a certain branch.
        Available parameters:
        n: limit number
        to, from: timestamp
        """
        url = self.gerrit.url('REFLOG', project_name=project, branch_id=branch)
        r = Request(method='GET', url=url, auth=self.gerrit.auth, params=query)
        return self.gerrit.dispatch(r)

    def list_child_projects(self, project):
        """List the direct child projects of a project."""
        url = self.gerrit.url('LIST_CHILD_PROJECTS', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_child_project(self, project, child_project, recursive=False):
        """Retrieves a child project. If a non-direct child project should be
        retrieved the parameter `recursive` must be set."""
        url = self.gerrit.url(
            'CHILD_PROJECT', project_name=project, child_project=child_project)
        if recursive:
            url += '?recursive'
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_tags(self, project):
        """List the tags of a project.
        Only includes tags under the refs/tags/ namespace."""
        url = self.gerrit.url('LIST_TAGS', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_tag(self, project, tag):
        """Retrieves a tag of a project."""
        url = self.gerrit.url('GET_TAG', project_name=project, tag=tag)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_commit(self, project, commit):
        """Retrieves a commit of a project."""
        url = self.gerrit.url(
            'GET_COMMIT', project_name=project, commit_id=commit)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_branch_content(self, project, commit, file):
        """Gets the content of a file from a certain commit.
        The content is returned as base64 encoded string."""
        url = self.gerrit.url(
            'COMMIT_CONTENT',
            project_name=project,
            commit_id=commit,
            file_id=file)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_dashboards(self, project):
        """List custom dashboards for a project."""
        url = self.gerrit.url('LIST_DASHBOARDS', project_name=project)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_dashboard(self, project, dashboard='default'):
        """List custom dashboards for a project."""
        url = self.gerrit.url(
            'DASHBOARD', project_name=project, dashboard_id=dashboard)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_dashboard(self, project, dashboard, dashboard_info):
        """Updates/Creates a project dashboard.
        Currently only supported for the default dashboard."""
        url = self.gerrit.url(
            'DASHBOARD', project_name=project, dashboard_id=dashboard)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=dashboard_info)
        return self.gerrit.dispatch(r)

    def delete_dashboard(self, project, dashboard, dashboard_info):
        """Deletes a project dashboard.
         Currently only supported for the default dashboard."""
        url = self.gerrit.url(
            'DASHBOARD', project_name=project, dashboard_id=dashboard)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
