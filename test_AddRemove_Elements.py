from selenium.webdriver.common.keys import Keys
from Pages.page_base import PageBase
import time



def test_addremove_elements_link_works(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link('Add/Remove Elements')
    url = page_obj.getUrl()
    page_obj.verifyUrlMatches(url, '/add_remove_elements/')
    page_obj.teardown()


