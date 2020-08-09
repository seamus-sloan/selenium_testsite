from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


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

    def goto(self, url):
        self.driver.get(url)

    def find(self, func, info):
        try:
            func(info)
        except NoSuchElementException:
            self.teardown()
            raise NoSuchElementException("Could not find element '{}' through '{}'".format(info, str(func.__name__)))
            
    def elementByClass(self, className):
        return self.driver.find_element_by_class_name(className)

    def elementByText(self, text):
        return self.driver.find_element_by_text(text)

    def elementByTag(self, tagName):
        return self.driver.find_element_by_tag_name(tagName)

    def elementById(self, id):
        return self.driver.find_element_by_id(id)
