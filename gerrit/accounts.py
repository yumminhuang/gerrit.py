# -*- coding: utf-8 -*-

from requests import Request

URLS = {
    # Account
    'SUGGEST_ACCOUNT': 'a/accounts/',
    'GET_ACCOUNT': 'a/accounts/%(account_id)s',
    'PUT_ACCOUNT': 'a/accounts/%(username)s',
    'ACCOUNT_NAME': 'a/accounts/%(account_id)s/name',
    'ACCOUNT_USERNAME': 'a/accounts/%(account_id)s/username',
    # Active
    'ACCOUNT_ACTIVE': 'a/accounts/%(account_id)s/active',
    # HTTP Password
    'HTTP_PASSWORD': 'a/accounts/%(account_id)s/password.http',
    # Emails
    'EMAILS': 'a/accounts/%(account_id)s/emails',
    'EMAIL': 'a/accounts/%(account_id)s/emails/%(email)s',
    'PREFERRED_EMAIL': 'a/accounts/%(account_id)s/emails/%(email)s/preferred',
    # SSH keys
    'SSH_KEYS': 'a/accounts/%(account_id)s/sshkeys',
    'SSH_KEY': 'a/accounts/%(account_id)s/sshkeys/%(key_id)s',
    # Capabilities
    'ACCOUNT_CAPABILITIES': 'a/accounts/%(account_id)s/capabilities',
    'ACCOUNT_CAPABILITY':
    'a/accounts/%(account_id)s/capabilities/%(capability)s',
    # Groups
    'GET_GROUPS': 'a/accounts/%(account_id)s/groups/',
    # Avatar
    'AVATAR': 'a/accounts/%(account_id)s/avatar',
    'AVATAR': 'a/accounts/%(account_id)s/avatar.change.url',
    'USER_PREFERENCES': 'a/accounts/%(account_id)s/preferences',
    'DIFF_PREFERENCES': 'a/accounts/%(account_id)s/preferences.diff',
    'STARED_CHANGES': 'a/accounts/%(account_id)s/starred.changes',
    'STAR_CHANGE': 'a/accounts/%(account_id)s/starred.changes/%(change_id)s'
}


class Accounts(object):
    """ This class provide account-related methods
    Account related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-accounts.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)

    def suggest_account(self, account, limit=10):
        """Suggest users for a given query q and result limit n.
        """
        url = self.gerrit.url('SUGGEST_ACCOUNT')
        r = Request(
            method='GET',
            url=url,
            auth=self.gerrit.auth,
            params={'q': account,
                    'limit': limit})
        return self.gerrit.dispatch(r)

    def get_account(self, account='self'):
        """Returns an account
        """
        url = self.gerrit.url('GET_ACCOUNT', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def create_account(self, account, **kwargs):
        # TODO: implement it
        pass

    def get_account_name(self, account='self'):
        """Retrieves the username of an account.
        """
        url = self.gerrit.url('ACCOUNT_NAME', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_account_name(self, account='self', name=None):
        """Sets the full name of an account.
        """
        url = self.gerrit.url('ACCOUNT_NAME', account_id=account)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'name': name})
        return self.gerrit.dispatch(r)

    def delete_account_name(self, account='self'):
        """Deletes the name of an account.
        """
        url = self.gerrit.url('ACCOUNT_NAME', account_id=account)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_account_username(self, account='self'):
        """Retrieves the username of an account.
        """
        url = self.gerrit.url('ACCOUNT_USERNAME', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_account_active(self, account='self'):
        """Checks if an account is active.
        """
        url = self.gerrit.url('ACCOUNT_ACTIVE', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_account_active(self, account='self'):
        """Sets the account state to active.
        """
        url = self.gerrit.url('ACCOUNT_ACTIVE', account_id=account)
        r = Request(method='PUT', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def delete_account_active(self, account='self'):
        """Sets the account state to inactive.
        """
        url = self.gerrit.url('ACCOUNT_ACTIVE', account_id=account)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_account_http_password(self, account='self'):
        """Retrieves the HTTP password of an account.
        """
        url = self.gerrit.url('HTTP_PASSWORD', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_account_http_password(self, account='self'):
        """Sets/Generates the HTTP password of an account.
        """
        url = self.gerrit.url('HTTP_PASSWORD', account_id=account)
        r = Request(
            method='PUT',
            url=url,
            auth=self.gerrit.auth,
            headers={'Content-Type': 'application/json; charset=UTF-8'},
            data={'generate': True})
        return self.gerrit.dispatch(r)

    def delete_account_http_password(self, account='self'):
        """Deletes the HTTP password of an account.
        """
        url = self.gerrit.url('HTTP_PASSWORD', account_id=account)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_account_emails(self, account='self'):
        """ Returns the email addresses that are configured for the
        specified user.
        """
        url = self.gerrit.url('EMAILS', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_account_email(self, account='self', email=None):
        """ Retrieves an email address of a user.
        """
        url = self.gerrit.url('EMAIL', account_id=account, email=email)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def add_account_email(self, account='self', email=None):
        """ Registers a new email address for the user.
        """
        url = self.gerrit.url('EMAIL', account_id=account, email=email)
        r = Request(method='PUT', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def delete_account_email(self, account='self', email=None):
        """ Deletes an email address of an account.
        """
        url = self.gerrit.url('EMAIL', account_id=account, email=email)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def set_account_preferred_email(self, account='self', email=None):
        """ Sets an email address as preferred email address for an account.
        """
        url = self.gerrit.url(
            'PREFERRED_EMAIL', account_id=account, email=email)
        r = Request(method='PUT', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_ssh_keys(self, account='self'):
        """ Get all ssh public keys associated with the given account.
        """
        url = self.gerrit.url('SSH_KEYS', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_ssh_key(self, account='self', key_id=None):
        """ Get one of the ssh keys associated with your account.
        """
        url = self.gerrit.url('SSH_KEY', account_id=account, key_id=key_id)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def add_ssh_key(self, account='self', key=None, key_id=None):
        """ Adds an SSH key for a user.
        """
        url = self.gerrit.url('SSH_KEYS', account_id=account)
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
        url = self.gerrit.url('SSH_KEY', account_id=account, key_id=key_id)
        r = Request(method='DELETE', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def list_account_capabilities(self, account='self', *capabilities):
        """ Returns the global capabilities that are enabled for the specified
        user.
        """
        url = self.gerrit.url('ACCOUNT_CAPABILITIES', account_id=account)
        r = Request(
            method='GET',
            url=url,
            auth=self.gerrit.auth,
            params={'q': capabilities})
        return self.gerrit.dispatch(r)

    def get_account_capability(self, account='self', capability=None):
        """ Checks if a user has a certain global capability.
        """
        url = self.gerrit.url(
            'ACCOUNT_CAPABILITY', account_id=account, capability=capability)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)

    def get_account_groups(self, account='self'):
        """Lists all groups that contain the specified user as a member."""
        url = self.gerrit.url('GET_GROUPS', account_id=account)
        r = Request(method='GET', url=url, auth=self.gerrit.auth)
        return self.gerrit.dispatch(r)
