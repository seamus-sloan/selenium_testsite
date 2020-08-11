from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:
    # Initialize webdriver based on user's runtime arguments
    def __init__(self, browser):
        if(browser.upper() == "CHROME"):
            self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        else:
            self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def getUrl(self):
        return self.driver.current_url

    def goto(self, url):
        self.driver.get(url)

    def click(self, element, times=1):
        for _ in range(0, times):
            element.click()

    def waitFor(self, seconds):
        WebDriverWait(self.driver, seconds)

    def find(self, func, info):
        try:
            return func(info)
        except NoSuchElementException:
            self.teardown()
            exceptionText = f"Could not find '{info}' through '{func.__name__}'"
            raise NoSuchElementException(exceptionText)

    # region Find Element
    def findButtonByText(self, buttonText):
        try:
            xpath = '//button[normalize-space()="{}"]'.format(buttonText)
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            self.teardown()
            exceptionText = f"Could not find '{buttonText}' button"
            raise NoSuchElementException(exceptionText)

    def elementByClass(self, className):
        return self.driver.find_element_by_class_name(className)

    def elementByText(self, text):
        return self.driver.find_element_by_text(text)

    def elementByTag(self, tagName):
        return self.driver.find_element_by_tag_name(tagName)

    def elementById(self, id):
        return self.driver.find_element_by_id(id)

    def elementByLinkText(self, linkText):
        return self.driver.find_element_by_link_text(linkText)
    # endregion

    # region Find Elements
    def elementsByClass(self, className):
        return self.driver.find_elements_by_class_name(className)

    def elementsByText(self, text):
        return self.driver.find_elements_by_text(text)

    def elementsByTag(self, tagName):
        return self.driver.find_elements_by_tag_name(tagName)

    def elementsById(self, id):
        return self.driver.find_elements_by_id(id)

    def elementsByLinkText(self, linkText):
        return self.driver.find_elements_by_link_text(linkText)
# endregion
