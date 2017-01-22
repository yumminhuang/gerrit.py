# -*- coding: utf-8 -*-

URLS = {}


class Projects(object):
    """ This class provide projects-related methods
    Projects related REST endpoints:
    https://gerrit-review.googlesource.com/Documentation/rest-api-projects.html
    """

    def __init__(self, gerrit):
        self.gerrit = gerrit
        self.gerrit.URLS.update(URLS)
