# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Change Endpoints
    'CHANGES':
    'a/changes/',
    'CHANGE':
    'a/changes/%(change_id)s',
    'CHANGE_DETAIL':
    'a/changes/%(change_id)s/detail',
    'CHANGE_TOPIC':
    'a/changes/%(change_id)s/topic',
    'ABANDON_CHANGE':
    'a/changes/%(change_id)s/abandon',
    'RESTORE_CHANGE':
    'a/changes/%(change_id)s/restore',
    'REBASE_CHANGE':
    'a/changes/%(change_id)s/rebase',
    'REVERT_CHANGE':
    'a/changes/%(change_id)s/revert',
    'SUBMIT_CHANGE':
    'a/changes/%(change_id)s/submit',
    'PUBLISH_CHANGE':
    'a/changes/%(change_id)s/publish',
    'INCLUDE_CHANGE':
    'a/changes/%(change_id)s/in',
    'INDEX_CHANGE':
    'a/changes/%(change_id)s/index',
    'CHECK_CHANGE':
    'a/changes/%(change_id)s/check',
    # Change Edit Endpoints
    'EIDT_CHANGE':
    'a/changes/%(change_id)s/edit',
    # Reviewer Endpoints
    'REVIEWERS':
    'a/changes/%(change_id)s/reviewers',
    'SUGGEST_REVIEWERS':
    'a/changes/%(change_id)s/suggest_reviewers',
    'REVIEWER':
    'a/changes/%(change_id)s/reviewers/%(account_id)s',
    # Revision Endpoints
    'COMMIT':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/commit',
    'REVISION_ACTION':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/actions',
    'COMMIT_REVIEW':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/review',
    'RELATED_CHANGES':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/related',
    'REBASE_REVISION':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/rebase',
    'SUBMIT_REVISION':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/submit',
    'PUBLISH_REVISION':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/publish',
    'DRAFT_REVISION':
    'a/changes/%(change_id)s/revisions/%(revision_id)s',
    'PATCH':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/patch',
    'REVISION_MERGEABLE':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/mergeable',
    'SUBMIT_TYPE':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/submit_type',
    'TEST_SUBMIT_TYPE':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/test.submit_type',
    'TEST_SUBMIT_RULE':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/test.submit_rule',
    'DRAFTS':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/drafts/',
    'DRAFT':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/drafts/%(draft_id)s',
    'COMMENTS':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/comments/',
    'COMMENT':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/comments/%(comment_id)s',
    'FILES':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/files/',
    'CHANGE_CONTENT':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/content',
    'CHANGE_DIFF':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/diff',
    'REVIEWED':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/reviewed',
    'CHERRYPICK':
    'a/changes/%(change_id)s/revisions/%(revision_id)s/cherrypick',
}


class Changes(object):
    """ This class provide change-related methods
    Change related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def query_changes(self, query_string, limit=10):
        """Queries changes visible to the caller. """
        url = self.gerrit.url('CHANGES')
        r = Request(
            method='GET',
            url=url,
            auth=self.gerrit.auth,
            params={'q': query_string,
                    'n': limit})
        return self.gerrit.dispatch(r)

    def get_change(self, change_id):
        """ Retrieves a change. """
        url = self.gerrit.url('CHANGE', change_id=change_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_change_detail(self, change_id):
        """ Retrieves a change with labels, detailed labels,
        detailed accounts, and messages. """
        url = self.gerrit.url('CHANGE_DETAIL', change_id=change_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
