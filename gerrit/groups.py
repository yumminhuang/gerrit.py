# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Group Endpoints
    'LIST_GROUPS': 'groups/',
    'GROUP': 'groups/%(group_id)s',
    'GET_GROUP_DETAIL': 'groups/%(group_id)s/detail',
    'GROUP_NAME': 'groups/%(group_id)s/name',
    'GROUP_DESCRIPTION': 'groups/%(group_id)s/description',
    'GROUP_OPTIONS': 'groups/%(group_id)s/options',
    'GROUP_OWNER': 'groups/%(group_id)s/owner',
    # Group Member Endpoints
    'GROUP_MEMBERS': 'groups/%(group_id)s/members',
    'GROUP_MEMBER': 'groups/%(group_id)s/members/%(account_id)s',
    # Group Include Endpoints
    'INCLUDED_GROUPS': 'groups/%(group_id)s/groups/',
    'INCLUDE_GROUP': 'groups/%(group_id)s/groups/%(sub_group_id)s/',
    'DELETE_INCLUDED_GROUPS': 'groups/%(group_id)s/groups.delete',
}


class Groups(object):
    """ This class provide groups-related methods
    Groups related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-groups.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list_groups(self, limit=None, skip=None):
        url = self.gerrit.url('LIST_GROUPS')
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
