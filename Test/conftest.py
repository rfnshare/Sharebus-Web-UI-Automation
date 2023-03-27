import pytest
from Resources.BrowserUtil.Browser import Browser
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = Browser()
    browser.launch_browser()
    browser.maximize_browser()
    browser.go_to_url()
    request.cls.driver = browser.get_web_driver()
    yield
    browser.close_browser()
