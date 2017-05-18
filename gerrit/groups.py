# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Group Endpoints
    'LIST_GROUPS': 'a/groups/',
    'GROUP': 'a/groups/%(group_id)s',
    'GROUP_DETAIL': 'a/groups/%(group_id)s/detail',
    'GROUP_NAME': 'a/groups/%(group_id)s/name',
    'GROUP_DESCRIPTION': 'a/groups/%(group_id)s/description',
    'GROUP_OPTIONS': 'a/groups/%(group_id)s/options',
    'GROUP_OWNER': 'a/groups/%(group_id)s/owner',
    # Group Member Endpoints
    'GROUP_MEMBERS': 'a/groups/%(group_id)s/members/',
    'GROUP_MEMBER': 'a/groups/%(group_id)s/members/%(account_id)s',
    # Group Include Endpoints
    'INCLUDE_GROUPS': 'a/groups/%(group_id)s/groups/',
    'INCLUDE_GROUP': 'a/groups/%(group_id)s/groups/%(sub_group_id)s/',
    'DELETE_INCLUDED_GROUPS': 'a/groups/%(group_id)s/groups.delete',
}


class Groups(object):
    """ This class provide groups-related methods
    Groups related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-groups.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list_groups(self, **query):
        """Lists the groups accessible by the caller.
        Available parameters:
        n: limit number
        S: skip number
        q: query keyword
        """
        # TODO: list_groups cannot parse `owned` option due to Requests defect
        # See: https://github.com/kennethreitz/requests/issues/2651
        url = self.gerrit.url('LIST_GROUPS')
        r = Request(method='GET', url=url, auth=self.gerrit.auth, params=query)
        return self.gerrit.dispatch(r)

    def get_group(self, group_id):
        """Retrieves a group."""
        url = self.gerrit.url('GROUP', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def create_group(self, group_name):
        """Creates a new Gerrit internal group."""
        url = self.gerrit.url('GROUP', group_id=group_name)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'})
        return self.gerrit.dispatch(r)

    def get_group_detail(self, group_id):
        """Retrieves a group with the direct members
        and the directly included groups."""
        url = self.gerrit.url('GROUP_DETAIL', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_group_name(self, group_id):
        """Retrieves the name of a group."""
        url = self.gerrit.url('GROUP_NAME', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def rename_group_name(self, group_id, group_name):
        """Renames a Gerrit internal group."""
        url = self.gerrit.url('GROUP_NAME', group_id=group_id)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'name': group_name})
        return self.gerrit.dispatch(r)

    def get_group_description(self, group_id):
        """Retrieves the description of a group."""
        url = self.gerrit.url('GROUP_DESCRIPTION', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_group_description(self, group_id, group_description):
        """Sets the description of a Gerrit internal group."""
        url = self.gerrit.url('GROUP_DESCRIPTION', group_id=group_id)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'description': group_description})
        return self.gerrit.dispatch(r)

    def delete_group_description(self, group_id):
        """Deletes the description of a Gerrit internal group.
        """
        url = self.gerrit.url('GROUP_DESCRIPTION', group_id=group_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_group_options(self, group_id):
        """Retrieves the options of a group."""
        url = self.gerrit.url('GROUP_OPTIONS', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_group_options(self, group_id, group_options):
        """Sets the options of a Gerrit internal group."""
        url = self.gerrit.url('GROUP_OPTIONS', group_id=group_id)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data=group_options)
        return self.gerrit.dispatch(r)

    def get_group_onwer(self, group_id):
        """Retrieves the options of a group."""
        url = self.gerrit.url('GROUP_OWNER', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_group_onwer(self, group_id, owner_group_id):
        """Retrieves the options of a group."""
        url = self.gerrit.url('GROUP_OWNER', group_id=group_id)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'owner': owner_group_id})
        return self.gerrit.dispatch(r)

    def list_group_members(self, group_id, recursive=False):
        """Lists the direct members of a Gerrit internal group."""
        url = self.gerrit.url('GROUP_MEMBERS', group_id=group_id)
        if recursive:
            url += '?recursive'
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_group_member(self, group_id, account_id):
        """Retrieves a group member."""
        url = self.gerrit.url(
            'GROUP_MEMBER', group_id=group_id, account_id=account_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def add_group_member(self, group_id, account_id):
        """Adds a user as member to a Gerrit internal group."""
        url = self.gerrit.url(
            'GROUP_MEMBER', group_id=group_id, account_id=account_id)
        r = Request(method='PUT', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def add_group_members(self, group_id, account_emails):
        """Adds one or several users to a Gerrit internal group."""
        url = self.gerrit.url('GROUP_MEMBERS', group_id=group_id)
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'members': account_emails})
        return self.gerrit.dispatch(r)

    def delete_group_member(self, group_id, account_id):
        """Deletes a user from a Gerrit internal group."""
        url = self.gerrit.url(
            'GROUP_MEMBER', group_id=group_id, account_id=account_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_included_groups(self, group_id):
        """Lists the directly included groups of a group."""
        url = self.gerrit.url('INCLUDE_GROUPS', group_id=group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_included_group(self, group_id, sub_group_id):
        """Retrieves an included group."""
        url = self.gerrit.url(
            'INCLUDE_GROUP', group_id=group_id, sub_group_id=sub_group_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def include_group(self, group_id, sub_group_id):
        """Includes an internal or external group into a Gerrit internal group. """
        url = self.gerrit.url(
            'INCLUDE_GROUP', group_id=group_id, sub_group_id=sub_group_id)
        r = Request(method='PUT', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def include_groups(self, group_id, sub_groups):
        """Includes one or several groups into a Gerrit internal group."""
        url = self.gerrit.url('INCLUDE_GROUPS', group_id=group_id)
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'groups': sub_groups})
        return self.gerrit.dispatch(r)

    def delete_included_group(self, group_id, sub_group_id):
        """Deletes an included group from a Gerrit internal group."""
        url = self.gerrit.url(
            'INCLUDE_GROUP', group_id=group_id, sub_group_id=sub_group_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def delete_included_groups(self, group_id, sub_groups):
        """Delete one or several included groups from a Gerrit internal group."""
        url = self.gerrit.url('DELETE_INCLUDED_GROUPS', group_id=group_id)
        r = Request(
            method='POST',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'groups': sub_groups})
        return self.gerrit.dispatch(r)
