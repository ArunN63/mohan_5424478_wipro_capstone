from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.basepage import BasePage


class HomePage(BasePage):

    BUY_MEDICINES_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Buy Medicines')]"
    )

    HOME_LOGO = (
        By.XPATH,
        "//img[contains(@src,'apollo247.svg')]"
    )

    POPUP_CLOSE_BUTTON = (
        By.XPATH,
        "//button//*[name()='svg']"
    )

    def close_popup_if_present(self):

        try:

            popup = self.wait_until_clickable(
                self.POPUP_CLOSE_BUTTON,
                5
            )

            self.driver.execute_script(
                "arguments[0].click();",
                popup
            )

            print("Popup closed successfully")

        except Exception:

            print("Popup not displayed")

    def click_buy_medicines(self):

        self.close_popup_if_present()

        medicine_btn = self.wait_until_clickable(
            self.BUY_MEDICINES_BUTTON,
            20
        )

        ActionChains(self.driver).move_to_element(
            medicine_btn
        ).perform()

        self.driver.execute_script(
            "arguments[0].click();",
            medicine_btn
        )

        print("Clicked Buy Medicines")

    def is_homepage_loaded(self):

        return self.is_displayed(
            self.HOME_LOGO
        )