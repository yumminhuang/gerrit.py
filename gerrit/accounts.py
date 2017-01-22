# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # SSH keys
    'GET_SSH_KEYS': 'accounts/%(account_id)s/sshkeys',
    'GET_SSH_KEY': 'accounts/%(account_id)s/sshkeys/%(key_id)s',
    'POST_SSH_KEY': 'accounts/%(account_id)s/sshkeys',
    'DELETE_SSH_KEY': 'accounts/%(account_id)s/sshkeys/%(key_id)s',
}


class Accounts(object):
    """ This class provide account-related methods
    Account related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-accounts.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def list_ssh_keys(self, account='self'):
        """ Get all ssh public keys associated with the given account.
        """
        url = self.gerrit.url('GET_SSH_KEYS', account_id=account)
        r = Request(
                method='GET',
                url=url,
                auth=self.gerrit.auth,
                headers={'Content-Type': 'application/json; charset=UTF-8'})
        return self.gerrit.dispatch(r)

    def get_ssh_key(self, account='self', key_id=None):
        """ Get one of the ssh keys associated with your account.
        """
        url = self.gerrit.url('GET_SSH_KEY', account_id=account, key_id=key_id)
        r = Request(
                method='GET',
                url=url,
                auth=self.gerrit.auth,
                headers={'Content-Type': 'application/json; charset=UTF-8'})
        return self.gerrit.dispatch(r)

    def add_ssh_key(self, account='self', key=None, key_id=None):
        """ Adds an SSH key for a user.
        """
        url = self.gerrit.url('POST_SSH_KEY', account_id=account)
        r = Request(
                method='POST',
                url=url,
                auth=self.gerrit.auth,
                headers={'Content-Type': 'plain/text'},
                data='%s %s' % (key, key_id))
        return self.gerrit.dispatch(r)

    def delete_ssh_key(self, account='self', key_id=None):
        """Deletes an SSH key of a user
        """
        url = self.gerrit.url('DELETE_SSH_KEY',
                              account_id=account,
                              key_id=key_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
