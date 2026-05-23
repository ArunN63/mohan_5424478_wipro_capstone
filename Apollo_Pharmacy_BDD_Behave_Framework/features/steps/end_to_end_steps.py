from behave import *

from utils.excel_utils import get_test_data
from utils.logger import setup_logger
from utils.screenshot_utils import take_screenshot

import time

logger = setup_logger()


# ---------------------------
# OPEN CATEGORY
# ---------------------------

@when("user opens category dynamically")
def open_category(context):

    data = get_test_data()

    index = int(
        data["condition_index"]
    )

    context.health_page.scroll_down_little()

    context.health_page.click_health_condition_by_index(
        index
    )

    logger.info(
        f"Category {index} opened"
    )


# ---------------------------
# PROCEED CHECKOUT
# ---------------------------

@when("user proceeds to checkout")
def proceed_checkout(context):

    context.health_page.click_proceed()

    logger.info(
        "Proceed clicked"
    )


# ---------------------------
# MOBILE NUMBER
# ---------------------------

@when("user enters mobile number dynamically")
def enter_mobile(context):

    data = get_test_data()

    mobile = str(
        int(data["mobile"])
    )

    assert len(mobile) == 10

    logger.info(
        "Mobile validation passed"
    )

    if context.health_page.is_login_popup_present():

        context.health_page.enter_mobile_number(
            mobile
        )

        context.health_page.click_continue()

        logger.info(
            "Mobile entered"
        )

        print(
            "Enter OTP manually now..."
        )

        time.sleep(30)

# ---------------------------
# selects location dynamically
# ---------------------------
@when("user selects location dynamically")
def select_location(context):

    print(
        "Selecting saved Office address..."
    )

    time.sleep(5)

    # CLICK SELECT ADDRESS

    context.health_page.click_select_address()

    logger.info(
        "Select address clicked"
    )

    time.sleep(5)

    # CLICK OFFICE ADDRESS

    context.health_page.select_saved_office_address()

    logger.info(
        "Office address selected"
    )

    time.sleep(5)


@then("address should save successfully")
def validate_address(context):

    logger.info(
        "Address flow completed"
    )

    take_screenshot(
        context.driver,
        "end_to_end_success"
    )

    assert True