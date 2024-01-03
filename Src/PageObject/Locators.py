from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    NAVBAR = (By.CSS_SELECTOR, "span[class*='text-success']")


class MyBusesLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in ']")
    NAVBAR = (By.XPATH, "//h1")
