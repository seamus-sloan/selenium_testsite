import pytest
from Pages.selenium_base import SeleniumBase


class PageBase(SeleniumBase):
    HOME = 'http://the-internet.herokuapp.com'

    def goto_home(self):
        self.goto(self.HOME)

    def goto_link(self, linkText):
        link = self.find(self.elementByLinkText, linkText)
        self.click(link)

    def assertEqual(self, actual, expected):
        try:
            assert(actual == expected)
        except Exception:
            self.teardown()
            raise Exception("'{}' did not match expected '{}'".format(actual, expected))

    def verifyUrlMatches(self, url, expected):
        self.assertEqual(url, self.HOME + expected)

    def verifyTextMatches(self, text, expected):
        self.assertEqual(text, expected)
