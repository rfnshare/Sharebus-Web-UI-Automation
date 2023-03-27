import inspect
from datetime import datetime
from pathlib import Path
import pytest
from selenium.webdriver.support.select import Select
import logging.config


@pytest.mark.usefixtures("setup")
class WebDriverSetup:
    def get_logger(self):
        file = logging.FileHandler(Path(__file__).parent.parent.parent/"Reports/Logs/logfile.log")  # File for log
        logging.basicConfig(datefmt='%Y-%m-%d %I:%M:%S %p')
        formatter = logging.Formatter("%(levelname)s :%(name)s :%(message)s :%(asctime)s")  # Format of log
        file.setFormatter(formatter)  # set formatter into file

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.addHandler(file)  # adding log into file
        logger.setLevel(logging.INFO)
        return logger

    def take_ss(self, name):
        SS_PATH = Path(__file__).parent / "../../Reports/Screenshots"
        self.driver.get_screenshot_as_file(SS_PATH / name)
