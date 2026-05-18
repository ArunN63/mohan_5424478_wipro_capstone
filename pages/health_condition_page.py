from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.basepage import BasePage

import time


class HealthConditionPage(BasePage):

    PRODUCT_SECTION = (
        By.XPATH,
        "//div[contains(@class,'ProductCard_productCardGrid__')]"
    )

    FILTER_HEADING = (
        By.XPATH,
        "//h3[contains(text(),'Filters')]"
    )

    CATEGORY_FILTER = (
        By.XPATH,
        "//p[contains(text(),'Category')]"
    )

    def scroll_down_little(self):

        self.driver.execute_script(
            "window.scrollBy(0, 500);"
        )

        time.sleep(3)

        print("Scrolled little down")

    def click_health_condition_by_index(self, index):

        dynamic_xpath = (
            By.XPATH,
            f"//*[@id='Browse by Health Conditions Web']/div[2]/div[{index}]/div/a"
        )

        condition = self.wait_until_clickable(
            dynamic_xpath,
            20
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            condition
        )

        time.sleep(2)

        ActionChains(self.driver).move_to_element(
            condition
        ).perform()

        self.driver.execute_script(
            "arguments[0].click();",
            condition
        )

        print(f"Clicked condition card {index}")

        time.sleep(5)

    def is_product_page_loaded(self):

        return self.is_displayed(
            self.PRODUCT_SECTION
        )

    def validate_filters_visible(self):

        return self.is_displayed(
            self.FILTER_HEADING
        )

    def click_category_filter(self):

        category = self.wait_until_clickable(
            self.CATEGORY_FILTER,
            20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            category
        )

        print("Category filter clicked")

        time.sleep(3)