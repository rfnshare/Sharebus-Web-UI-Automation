import inspect
from datetime import datetime
from pathlib import Path
import pytest
from selenium.webdriver.support.select import Select
import logging.config


@pytest.mark.usefixtures("setup")
class WebDriverSetup:
    def get_logger(self):
        LOGGING_CONFIG = Path(__file__).parent.parent.parent / 'Config/logging.conf'
        logging.config.fileConfig(LOGGING_CONFIG)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger

    def take_ss(self, name):
        SS_PATH = Path(__file__).parent / "../../Reports/Screenshots"
        self.driver.get_screenshot_as_file(SS_PATH / name)
