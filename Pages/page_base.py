import pytest
from Pages.selenium_base import SeleniumBase


class PageBase(SeleniumBase):
    HOME = 'http://the-internet.herokuapp.com/'


    def goto_home(self):
        self.goto(self.HOME)
