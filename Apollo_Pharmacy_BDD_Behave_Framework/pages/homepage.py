from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import time


class HomePage:

    def __init__(self, driver):

        self.driver = driver

    # ---------------------------
    # HOMEPAGE VALIDATION
    # ---------------------------

    def is_homepage_loaded(self):

        return (
            "apollo"
            in self.driver.title.lower()
        )

    # ---------------------------
    # CLOSE POPUP
    # ---------------------------

    def close_popup_if_present(self):

        try:

            time.sleep(3)

            popup_close = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(@class,'close')]"
                    )
                )
            )

            popup_close.click()

            print(
                "Popup closed"
            )

        except TimeoutException:

            print(
                "No popup displayed"
            )

        except Exception as e:

            print(
                "Popup handling failed:",
                e
            )

    # ---------------------------
    # CLICK BUY MEDICINES
    # ---------------------------

    def click_buy_medicines(self):

        # CLOSE POPUP FIRST

        self.close_popup_if_present()

        button = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(text(),'Buy Medicines')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "Buy Medicines clicked"
        )