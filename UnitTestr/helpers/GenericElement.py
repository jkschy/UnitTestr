import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UnitTestr.helpers import Logger


class GenericElement:
    css = ""
    css_type: By = None
    element: WebElement = None
    browser: webdriver.Firefox = None

    def __init__(self, browser: webdriver.Firefox, selector_type: By, css: str, timeout_ms: int = 1000):
        """
        An interactible element on the screen
        :param browser: The Browser to look for the element
        :param selector_type: The type of selector
        :param css: the selector
        :param timeout_ms: the timeout
        """
        self.css_type = selector_type
        self.css = css
        self.browser = browser
        self.getElement(timeout_ms)

    def getElement(self, timeout):
        """
        Try to get the element within the browser
        :param timeout: the length of timeout
        :return True if the element was found
        :raise NoSuchElementException
        """
        try:
            self.element = WebDriverWait(self.browser, timeout / 1000).until(
                EC.element_to_be_clickable((self.css_type, self.css)))
            Logger.debug(f"Found element with {self.css_type} {self.css}")
            return True
        except selenium.common.exceptions.TimeoutException:
            raise selenium.common.exceptions.NoSuchElementException(f"Element with {self.css_type} {self.css} was not "
                                                                    f"found in the timeout")

    def click(self):
        """
        Tries to click the element
        """
        if self.element is None:
            self.getElement()

        self.element.click()

    def type(self, text):
        """
        Types the text into the element
        :param text: The text to type
        """
        if self.element is None:
            self.getElement(10000)

        self.element.send_keys(text)
        Logger.debug(f"Typed [\"{text}\"] on element with {self.css_type} {self.css}")
        assert self.getAttribute("value") == text, \
            f"[\"{text}\"] was not properly typed in on element with {self.css_type} {self.css}"

    def getAttribute(self, name):
        """
        Tries to get the attribute from the element
        :param name: the attribute name you want
        :return: the value of the attribute
        """
        return self.element.get_attribute(name)

    def text(self):
        return self.element.text

    def exists(self):
        """
        Checks if the element still exists
        :return: If the Element exists
        """
        try:
            return self.getElement(1)
        except selenium.common.exceptions.NoSuchElementException:
            return False