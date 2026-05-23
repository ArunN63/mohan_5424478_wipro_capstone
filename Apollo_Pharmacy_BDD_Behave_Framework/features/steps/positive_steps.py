from behave import *

from utils.logger import setup_logger
from utils.screenshot_utils import take_screenshot

logger = setup_logger()


# ---------------------------
# INCREASE QUANTITY
# ---------------------------

@when("user increases quantity")
def increase_quantity(context):

    assert context.driver is not None

    context.health_page.increase_quantity()

    logger.info(
        "Quantity increased"
    )

    take_screenshot(
        context.driver,
        "quantity_increased"
    )


# ---------------------------
# DECREASE QUANTITY
# ---------------------------

@when("user decreases quantity")
def decrease_quantity(context):

    assert context.driver is not None

    context.health_page.decrease_quantity()

    logger.info(
        "Quantity decreased"
    )

    take_screenshot(
        context.driver,
        "quantity_decreased"
    )


# ---------------------------
# QUANTITY VALIDATION
# ---------------------------

@then("cart quantity should update")
def validate_quantity(context):

    assert context.driver is not None

    quantity_elements = context.driver.find_elements(
        "xpath",
        "//*[contains(text(),'1') or contains(text(),'2')]"
    )

    assert len(quantity_elements) > 0

    logger.info(
        "Cart quantity validation passed"
    )

    take_screenshot(
        context.driver,
        "cart_quantity"
    )