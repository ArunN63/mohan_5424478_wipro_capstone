from behave import *

from utils.logger import setup_logger
from utils.screenshot_utils import take_screenshot

import time

logger = setup_logger()


# ---------------------------
# INVALID CATEGORY
# ---------------------------

@when('user opens invalid category "{index}"')
def invalid_category(context, index):

    assert context.driver is not None

    try:

        context.health_page.scroll_down_little()

        context.health_page.click_health_condition_by_index(
            int(index)
        )

    except Exception as e:

        context.error = e

        logger.info(
            f"Exception captured: {e}"
        )


# ---------------------------
# EXCEPTION VALIDATION
# ---------------------------

@then("exception should be handled")
def validate_exception(context):

    assert context.error is not None

    assert isinstance(
        context.error,
        Exception
    )

    logger.info(
        "Negative validation passed"
    )

    take_screenshot(
        context.driver,
        "invalid_category"
    )


# ---------------------------
# INVALID PAGE NAVIGATION
# ---------------------------

@when("user navigates to invalid page")
def invalid_page(context):

    assert context.driver is not None

    invalid_url = (
        context.driver.current_url
        + "?page=99"
    )

    context.driver.get(
        invalid_url
    )

    assert "page=99" in invalid_url

    logger.info(
        "Invalid page opened"
    )

    time.sleep(5)


# ---------------------------
# INVALID PAGE VALIDATION
# ---------------------------

@then("invalid page should be validated")
def validate_invalid_page(context):

    assert (
        "page=99"
        in context.driver.current_url
    )

    assert context.driver.current_url is not None

    logger.info(
        "Invalid page validation passed"
    )

    take_screenshot(
        context.driver,
        "invalid_page"
    )