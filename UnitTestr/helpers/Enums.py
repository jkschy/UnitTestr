from selenium.webdriver.common.by import By
from Tests.Workflows.User import User


class Locator_Type:
    """
    All the usable selector types
    """
    CSS = By.CSS_SELECTOR
    ID = By.ID
    X_PATH = By.XPATH
    CLASS = By.CLASS_NAME
