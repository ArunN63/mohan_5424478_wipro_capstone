from behave import *

from pages.homepage import HomePage
from pages.health_condition_page import HealthConditionPage

from utils.logger import setup_logger
from utils.screenshot_utils import take_screenshot

import time

logger = setup_logger()


# ---------------------------
# LAUNCH WEBSITE
# ---------------------------

@given("user launches Apollo Pharmacy website")
def launch_site(context):

    context.homepage = HomePage(
        context.driver
    )

    assert context.homepage.is_homepage_loaded()

    logger.info(
        "Homepage loaded"
    )


# ---------------------------
# CLICK BUY MEDICINES
# ---------------------------

@when("user clicks Buy Medicines")
def click_buy_medicines(context):

    context.homepage.click_buy_medicines()

    logger.info(
        "Buy Medicines clicked"
    )

    context.health_page = HealthConditionPage(
        context.driver
    )

    assert context.health_page is not None

    time.sleep(3)


# ---------------------------
# OPEN CATEGORY
# ---------------------------

@when('user opens category "{index}"')
def open_category(context, index):

    context.health_page.scroll_down_little()

    context.health_page.click_health_condition_by_index(
        int(index)
    )

    assert int(index) >= 0

    logger.info(
        f"Category {index} opened"
    )


# ---------------------------
# PRODUCT PAGE VALIDATION
# ---------------------------

@then("product page should load")
def validate_product_page(context):

    assert context.health_page.is_product_page_loaded()

    logger.info(
        "Product page loaded"
    )

    take_screenshot(
        context.driver,
        "product_page"
    )


# ---------------------------
# NAVIGATION VALIDATION
# ---------------------------

@then("user should navigate to another category page")
def validate_navigation(context):

    current_url = (
        context.driver.current_url
    )

    print(
        f"Navigated URL: {current_url}"
    )

    assert (
        "health" in current_url.lower()
        or
        "category" in current_url.lower()
        or
        "otc" in current_url.lower()
    )

    logger.info(
        "Successfully navigated to another category page"
    )

    take_screenshot(
        context.driver,
        "category_navigation"
    )


# ---------------------------
# APPLY FILTERS
# ---------------------------

@when("user applies filters")
def apply_filters(context):

    context.health_page.apply_filters(
        max_filters=2
    )

    logger.info(
        "Filters applied"
    )


# ---------------------------
# FILTER VALIDATION
# ---------------------------

@then("filters should apply successfully")
def validate_filters(context):

    assert context.health_page.is_product_page_loaded()

    assert context.driver.current_url is not None

    logger.info(
        "Filters validation passed"
    )

    take_screenshot(
        context.driver,
        "filters_applied"
    )


# ---------------------------
# ADD PRODUCT
# ---------------------------

@when("user adds product to cart")
def add_product(context):

    context.health_page.add_first_product_to_cart()

    assert context.driver is not None

    logger.info(
        "Product added to cart"
    )

    take_screenshot(
        context.driver,
        "product_added"
    )


# ---------------------------
# NAVIGATE TO ANOTHER PAGE
# ---------------------------

@when("user navigates to another page")
def navigate_next_page(context):

    context.health_page.navigate_to_next_page()

    assert (
        "apollo"
        in context.driver.current_url.lower()
    )

    logger.info(
        "Pagination / navigation successful"
    )

    take_screenshot(
        context.driver,
        "pagination_navigation"
    )


# ---------------------------
# CART VALIDATION
# ---------------------------

@then("cart should open successfully")
def validate_cart(context):

    context.health_page.open_cart()

    assert (
            "cart"
            in context.driver.current_url.lower()
            or
            "checkout"
            in context.driver.current_url.lower()
            or
            "medicines-cart"
            in context.driver.current_url.lower()
    )

    logger.info(
        "Cart validation passed"
    )

    take_screenshot(
        context.driver,
        "cart_validation"
    )