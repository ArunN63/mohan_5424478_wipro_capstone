from utils.driver_setup import get_driver
from pages.homepage import HomePage
from pages.health_condition_page import HealthConditionPage

import time


def test_health_conditions():

    driver = get_driver()

    homepage = HomePage(driver)

    assert homepage.is_homepage_loaded()

    print("Homepage loaded successfully")

    homepage.click_buy_medicines()

    print("Apollo Pharmacy opened successfully")

    health_page = HealthConditionPage(driver)

    time.sleep(5)

    health_page.scroll_down_little()

    condition_indexes = [1, 2, 3]

    for index in condition_indexes:

        print(f"Testing condition card {index}")

        health_page.click_health_condition_by_index(index)

        assert health_page.is_product_page_loaded()

        print(f"Condition card {index} page loaded successfully")

        assert health_page.validate_filters_visible()

        print("Filters section visible successfully")

        health_page.click_category_filter()

        print("Category filter validated successfully")

        driver.back()

        time.sleep(5)

        health_page.scroll_down_little()

    driver.quit()