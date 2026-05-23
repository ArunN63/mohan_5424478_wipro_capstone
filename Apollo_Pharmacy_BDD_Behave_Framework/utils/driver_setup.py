# utils/driver_setup.py

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


def get_driver():

    # ---------------------------
    # CHROME OPTIONS
    # ---------------------------

    options = webdriver.ChromeOptions()

    # INCOGNITO MODE

    options.add_argument(
        "--incognito"
    )

    # MAXIMIZE

    options.add_argument(
        "--start-maximized"
    )

    # DISABLE NOTIFICATIONS

    options.add_argument(
        "--disable-notifications"
    )

    # DISABLE POPUPS

    options.add_argument(
        "--disable-popup-blocking"
    )

    # REMOVE AUTOMATION INFOBAR

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    # ---------------------------
    # DRIVER
    # ---------------------------

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    # ---------------------------
    # WINDOW
    # ---------------------------

    driver.maximize_window()

    # ---------------------------
    # OPEN APOLLO
    # ---------------------------

    driver.get(
        "https://www.apollopharmacy.in/"
    )

    # ---------------------------
    # IMPLICIT WAIT
    # ---------------------------

    driver.implicitly_wait(10)

    return driver