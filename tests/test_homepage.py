from utils.driver_setup import get_driver
from pages.homepage import HomePage

import time


def test_homepage():

    driver = get_driver()

    homepage = HomePage(driver)

    assert homepage.is_homepage_loaded()

    print("Homepage loaded successfully")

    homepage.click_buy_medicines()

    print("Apollo Pharmacy page opened successfully")

    time.sleep(5)

    driver.quit()