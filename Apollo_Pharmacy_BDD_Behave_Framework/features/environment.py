from utils.driver_setup import get_driver
from utils.screenshot_utils import take_screenshot

import os


# ---------------------------
# BEFORE SCENARIO
# ---------------------------

def before_scenario(context, scenario):

    context.driver = get_driver()

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    os.makedirs(
        "reports/allure-results",
        exist_ok=True
    )

    print(
        f"\nStarting Scenario: {scenario.name}"
    )


# ---------------------------
# AFTER SCENARIO
# ---------------------------

def after_scenario(context, scenario):

    try:

        screenshot_name = (
            scenario.name
            .replace(" ", "_")
            .replace("/", "_")
        )

        take_screenshot(
            context.driver,
            screenshot_name
        )

        print(
            f"Screenshot captured: {screenshot_name}"
        )

    except Exception as e:

        print(
            "Screenshot capture failed:",
            e
        )

    finally:

        try:

            context.driver.quit()

            print(
                "Browser closed"
            )

        except Exception as e:

            print(
                "Driver quit failed:",
                e
            )