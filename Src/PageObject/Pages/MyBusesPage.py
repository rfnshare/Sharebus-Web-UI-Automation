from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import MyBusesLocators


class MyBusesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = MyBusesLocators

    def test(self):
        pass

