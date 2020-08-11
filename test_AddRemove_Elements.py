from Pages.page_base import PageBase
import time

LINK_TEXT = 'Add/Remove Elements'


"""f
def test_addremove_elements_link_works(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    url = page_obj.getUrl()
    page_obj.verifyMatches(url, page_obj.HOME + '/add_remove_elements/')


def test_add_button_creates_element(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 1)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.verifyMatches(len(elements), 1)


def test_delete_button_removes_element(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 1)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.click(elements[0])
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.verifyMatches(len(elements), 0)


def test_add_button_creates_multiple_elements(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 2)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.verifyMatches(len(elements), 2)


def test_delete_button_removes_multiple_elements(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 2)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.click(elements[0])
    page_obj.click(elements[1])
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.verifyMatches(len(elements), 0)


def test_add_button_works_after_deletion(browser):
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 1)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.click(elements[0])
    page_obj.click(button, 1)
    elements = page_obj.find(page_obj.elementsByClass, 'added-manually')
    page_obj.verifyMatches(len(elements), 1)
"""

def test_page_can_scale_down_when_filled_with_elements(browser):    
    page_obj = PageBase(browser)
    page_obj.goto_home()
    page_obj.goto_link(LINK_TEXT)
    button = page_obj.findButtonByText('Add Element')
    page_obj.click(button, 100000)
#     # After adding the as many elements as possible,
#     # shrink the window size as small as possible
#     # and verify the amount of columns displayed

# def page_can_scale_up_when_filled_with_elements(browser):
#     # After adding the as many elements as possible,
#     # enlarge the window size as much as possible
#     # and verify the amount of columns displayed
