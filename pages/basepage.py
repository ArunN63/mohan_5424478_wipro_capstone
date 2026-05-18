from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def wait_until_clickable(self, locator, timeout=10):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_visible(self, locator, timeout=10):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def is_displayed(self, locator, timeout=10):

        element = WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

        return element.is_displayed()

    def scroll_down(self):

        self.driver.execute_script(
            "window.scrollBy(0, 1200);"
        )