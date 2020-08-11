from Pages.page_base import PageBase

LINK_TEXT = 'A/B Testing'


def test_abtest_link_works(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    url = page_obj.getUrl()
    page_obj.verifyMatches(url, page_obj.HOME + '/abtest')
    page_obj.teardown()


"""
    The /abtest page seems to have two different versions
    Both versions can be seen if the page is refreshed multiple
    times, but one version always ends up staying (With header
    "A/B Test Control"). Due to this, the only way to automate
    this test would be to determine the cases where Version 1 
    of the page would appear vs Version 2. 

    Even after looking at the /the-internet repository, there was
    no answer on when the page changes
"""
# def test_abtest_header_version_one(browser):
#     page_obj = PageBase(browser)
#     page_obj.goto_home()
#     page_obj.goto_link(LINK_TEXT)
#     headerText = page_obj.find(page_obj.elementByTag, 'h3').text
#     page_obj.verifyTextMatches(headerText, 'A/B Test Variation 1') # Works 50% of the time
