import allure
import pytest
from Src.PageObject.Pages.MyBusesPage import MyBusesPage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("Login Test")
@allure.description("Checking Login Function")
class TestLoginPage(WebDriverSetup):
    @pytest.mark.smoke
    def test_01_login(self):
        log = self.get_logger()
        mybus_page = MyBusesPage(self.driver)
        assert "Sign in" in mybus_page.login()
        log.info("Login Page loaded successfully")

