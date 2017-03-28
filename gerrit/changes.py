# -*- coding: utf-8 -*-

URLS = {
    # Change Endpoints
    'CHANGES':
    'changes',
    'CHANGE':
    'changes/%(change_id)s',
    'CHANGE_DETAIL':
    'changes/%(change_id)s/detail',
    'CHANGE_TOPIC':
    'changes/%(change_id)s/topic',
    'ABANDON_CHANGE':
    'changes/%(change_id)s/abandon',
    'RESTORE_CHANGE':
    'changes/%(change_id)s/restore',
    'REBASE_CHANGE':
    'changes/%(change_id)s/rebase',
    'REVERT_CHANGE':
    'changes/%(change_id)s/revert',
    'SUBMIT_CHANGE':
    'changes/%(change_id)s/submit',
    'PUBLISH_CHANGE':
    'changes/%(change_id)s/publish',
    'INCLUDE_CHANGE':
    'changes/%(change_id)s/in',
    'INDEX_CHANGE':
    'changes/%(change_id)s/index',
    'CHECK_CHANGE':
    'changes/%(change_id)s/check',
    # Change Edit Endpoints
    'EIDT_CHANGE':
    'changes/%(change_id)s/edit',
    # Reviewer Endpoints
    'REVIEWERS':
    'changes/%(change_id)s/reviewers',
    'SUGGEST_REVIEWERS':
    'changes/%(change_id)s/suggest_reviewers',
    'REVIEWER':
    'changes/%(change_id)s/reviewers/%(account_id)s',
    # Revision Endpoints
    'COMMIT':
    'changes/%(change_id)s/revisions/%(revision_id)s/commit',
    'REVISION_ACTION':
    'changes/%(change_id)s/revisions/%(revision_id)s/actions',
    'COMMIT_REVIEW':
    'changes/%(change_id)s/revisions/%(revision_id)s/review',
    'RELATED_CHANGES':
    'changes/%(change_id)s/revisions/%(revision_id)s/related',
    'REBASE_REVISION':
    'changes/%(change_id)s/revisions/%(revision_id)s/rebase',
    'SUBMIT_REVISION':
    'changes/%(change_id)s/revisions/%(revision_id)s/submit',
    'PUBLISH_REVISION':
    'changes/%(change_id)s/revisions/%(revision_id)s/publish',
    'DRAFT_REVISION':
    'changes/%(change_id)s/revisions/%(revision_id)s',
    'PATCH':
    'changes/%(change_id)s/revisions/%(revision_id)s/patch',
    'REVISION_MERGEABLE':
    'changes/%(change_id)s/revisions/%(revision_id)s/mergeable',
    'SUBMIT_TYPE':
    'changes/%(change_id)s/revisions/%(revision_id)s/submit_type',
    'TEST_SUBMIT_TYPE':
    'changes/%(change_id)s/revisions/%(revision_id)s/test.submit_type',
    'TEST_SUBMIT_RULE':
    'changes/%(change_id)s/revisions/%(revision_id)s/test.submit_rule',
    'DRAFTS':
    'changes/%(change_id)s/revisions/%(revision_id)s/drafts/',
    'DRAFT':
    'changes/%(change_id)s/revisions/%(revision_id)s/drafts/%(draft_id)s',
    'COMMENTS':
    'changes/%(change_id)s/revisions/%(revision_id)s/comments/',
    'COMMENT':
    'changes/%(change_id)s/revisions/%(revision_id)s/comments/%(comment_id)s',
    'FILES':
    'changes/%(change_id)s/revisions/%(revision_id)s/files/',
    'CHANGE_CONTENT':
    'changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/content',
    'CHANGE_DIFF':
    'changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/diff',
    'REVIEWED':
    'changes/%(change_id)s/revisions/%(revision_id)s/files/%(file_id)s/reviewed',
    'CHERRYPICK':
    'changes/%(change_id)s/revisions/%(revision_id)s/cherrypick',
}


class Changes(object):
    """ This class provide change-related methods
    Change related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
