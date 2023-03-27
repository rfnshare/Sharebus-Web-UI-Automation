import allure

from Src.PageObject.Pages.HomePage import HomePage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("Home Page Test")
@allure.description("Checking homepage elements appears properly")
class TestHomePage(WebDriverSetup):
    def test_01_home_page_elements_visibility(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        print("Starting to check are all homepage elements visible properly")
        assert home_page.check_home_page_elements() is True, "Home page elements are not visible properly"
        log.info(f"URL {url} is loaded with {home_page.get_text()}")
        assert "failed" in home_page.get_text()
        log.critical("Title Not Matching")
