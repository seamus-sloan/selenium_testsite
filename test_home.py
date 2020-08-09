from selenium.webdriver.common.keys import Keys
from Pages.page_base import PageBase


def test_homepage_has_header(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.find(page_obj.elementById, 'flash-messages1')
    page_obj.teardown()


def test_homepage_has_footer(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.find(page_obj.elementById, 'page-footer1')
    page_obj.teardown()


def test_homepage_has_content(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.find(page_obj.elementById, 'content1')
    page_obj.teardown()
