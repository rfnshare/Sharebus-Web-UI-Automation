from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HomePageLocators

    def test(self):
        pass

