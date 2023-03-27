import allure

from Src.PageObject.Pages.HomePage import HomePage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("Home Page Test")
@allure.description("Checking homepage elements appears properly")
class TestHomePage(WebDriverSetup):
    def test_checking_home_is_loaded(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        home_page.get_navbar()
        log.info(f"URL {url} is loaded")
