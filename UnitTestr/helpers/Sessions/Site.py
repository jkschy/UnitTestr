from selenium import webdriver
from UnitTestr.helpers.Enums import By
from UnitTestr.helpers import GenericElement, JsonHelp


class Site:
    url: str = ""
    browser: webdriver = None
    _instance = None

    def __init__(self, url=None):
        """Starts a new Firefox Browser using webdriver and goes to the url

            :param url the url you want to start the browser at.
                    Note: appends url to the end of 'default_url' inside Config.json
        """
        self.browser = webdriver.Firefox()
        if url is None:
            self.browser.get(JsonHelp.getSetting("default_url"))
        elif JsonHelp.getSetting("default_url") != "":
            self.browser.get(JsonHelp.getSetting("default_url") + url)
        else:
            self.browser.get(url)

    def getElement(self, by: By, element_id: str, timeout_ms=10000):
        """
        Attemots to get an element from the default browser
        :param by: The css selector
        :param element_id: The Selector of the element you want
        :param timeout_ms: the timeout to wait
        :return: The Element
        """
        return GenericElement.GenericElement(self.browser, by, element_id, timeout_ms)

    def getNumElementsFromClass(self, class_name):
        return self.browser.find_elements(By.CLASS_NAME, class_name).__len__()

    def end(self):
        """
        Ends the current browser
        """
        self.browser.quit()
