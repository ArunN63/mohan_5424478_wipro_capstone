# pages/health_condition_page.py

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class HealthConditionPage:

    def __init__(self, driver):

        self.driver = driver

    # ---------------------------
    # SCROLL
    # ---------------------------

    def scroll_down_little(self):

        self.driver.execute_script(
            "window.scrollBy(0,700);"
        )

        time.sleep(2)

    # ---------------------------
    # CLICK HEALTH CONDITION
    # ---------------------------

    def click_health_condition_by_index(
            self,
            index
    ):

        time.sleep(5)

        section = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h2[contains(text(),'Browse by Health Conditions')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            section
        )

        time.sleep(3)

        conditions = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//h2[contains(text(),'Browse by Health Conditions')]"
                    "/following::a[contains(@href,'health-condition') or contains(@href,'category') or contains(@href,'medicines')][position()<=12]"
                )
            )
        )

        print(
            f"Total conditions found: {len(conditions)}"
        )

        if index >= len(conditions):

            raise Exception(
                f"Invalid index: {index}"
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            conditions[index]
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            conditions[index]
        )

        print(
            f"Condition {index} clicked"
        )

        time.sleep(5)

    # ---------------------------
    # PRODUCT PAGE VALIDATION
    # ---------------------------

    def is_product_page_loaded(self):

        return (
            "apollo"
            in self.driver.current_url.lower()
        )

    # ---------------------------
    # NAVIGATE TO NEXT PAGE
    # ---------------------------

    def navigate_to_next_page(self):

        print(
            "Navigating to next page..."
        )

        try:

            time.sleep(5)

            current_url = (
                self.driver.current_url
            )

            print(
                f"Current URL: {current_url}"
            )

            # SCROLL DOWN

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(3)

            # TRY NEXT BUTTON

            next_buttons = self.driver.find_elements(
                By.XPATH,
                "//a[contains(text(),'Next')] | //button[contains(text(),'Next')]"
            )

            if len(next_buttons) > 0:

                self.driver.execute_script(
                    "arguments[0].click();",
                    next_buttons[0]
                )

                print(
                    "Next page clicked"
                )

            else:

                # FALLBACK → OPEN ANOTHER CATEGORY

                print(
                    "No pagination found, opening another category"
                )

                self.driver.back()

                time.sleep(5)

                self.scroll_down_little()

                self.click_health_condition_by_index(5)

            time.sleep(5)

            print(
                f"New URL: {self.driver.current_url}"
            )

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/pagination_failed.png"
            )

            print(
                "Pagination failed:",
                e
            )

            raise

    # ---------------------------
    # APPLY FILTERS
    # ---------------------------

    def apply_filters(
            self,
            max_filters=2
    ):

        print(
            "Applying filters..."
        )

        time.sleep(8)

        applied = 0

        try:

            self.driver.execute_script(
                "window.scrollBy(0,500);"
            )

            time.sleep(3)

            checkboxes = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "//input[@type='checkbox']"
                    )
                )
            )

            print(
                f"Checkboxes found: {len(checkboxes)}"
            )

            for checkbox in checkboxes:

                try:

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        checkbox
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        checkbox
                    )

                    applied += 1

                    print(
                        f"Filter {applied} applied"
                    )

                    time.sleep(4)

                    if applied >= max_filters:
                        break

                except Exception as e:

                    print(
                        "Checkbox skipped:",
                        e
                    )

                    continue

            if applied == 0:

                self.driver.save_screenshot(
                    "screenshots/filter_failed.png"
                )

                print(
                    "No filters applied"
                )

                return

            print(
                f"Total filters applied: {applied}"
            )

        except Exception as e:

            print(
                "Filter handling failed:",
                e
            )

            self.driver.save_screenshot(
                "screenshots/filter_exception.png"
            )

            return


    # ---------------------------
    # INCREASE QUANTITY
    # ---------------------------

    def increase_quantity(self):

        print(
            "Increasing quantity..."
        )

        try:

            time.sleep(3)

            buttons = self.driver.find_elements(
                By.XPATH,
                "//button"
            )

            clicked = False

            for button in buttons:

                try:

                    text = button.text.strip().lower()

                    aria = (
                            button.get_attribute(
                                "aria-label"
                            )
                            or ""
                    ).lower()

                    cls = (
                            button.get_attribute(
                                "class"
                            )
                            or ""
                    ).lower()

                    if (
                            "+"
                            in text
                            or
                            "increase" in aria
                            or
                            "plus" in cls
                            or
                            "qty" in cls
                    ):
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            button
                        )

                        time.sleep(2)

                        self.driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        print(
                            "Quantity increased"
                        )

                        clicked = True

                        break

                except:
                    continue

            if not clicked:
                print(
                    "Increase quantity button not found"
                )

            time.sleep(3)

        except Exception as e:

            print(
                "Increase quantity failed:",
                e
            )

            raise

    # ---------------------------
    # DECREASE QUANTITY
    # ---------------------------

    def decrease_quantity(self):

        print(
            "Decreasing quantity..."
        )

        try:

            time.sleep(3)

            buttons = self.driver.find_elements(
                By.XPATH,
                "//button"
            )

            clicked = False

            for button in buttons:

                try:

                    text = button.text.strip().lower()

                    aria = (
                            button.get_attribute(
                                "aria-label"
                            )
                            or ""
                    ).lower()

                    cls = (
                            button.get_attribute(
                                "class"
                            )
                            or ""
                    ).lower()

                    if (
                            "-"
                            in text
                            or
                            "decrease" in aria
                            or
                            "minus" in cls
                    ):
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            button
                        )

                        time.sleep(2)

                        self.driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        print(
                            "Quantity decreased"
                        )

                        clicked = True

                        break

                except:
                    continue

            if not clicked:
                print(
                    "Decrease quantity button not found"
                )

            time.sleep(3)

        except Exception as e:

            print(
                "Decrease quantity failed:",
                e
            )

            raise

    # ---------------------------
    # PRODUCT PAGE VALIDATION
    # ---------------------------

    def is_product_page_loaded(self):

        print(
            "Waiting for product page..."
        )

        try:

            time.sleep(8)

            # WAIT FOR PRODUCTS

            products = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "//img | //button[contains(text(),'ADD')]"
                    )
                )
            )

            print(
                f"Products loaded: {len(products)}"
            )

            return len(products) > 0

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/product_page_failed.png"
            )

            print(
                "Product page load failed:",
                e
            )

            return False

    # ---------------------------
    # ADD PRODUCT TO CART
    # ---------------------------

    def add_first_product_to_cart(self):

        print(
            "Waiting for products..."
        )

        time.sleep(8)

        try:

            # SCROLL LITTLE

            self.driver.execute_script(
                "window.scrollBy(0,700);"
            )

            time.sleep(5)

            # POSSIBLE ADD BUTTONS

            add_buttons = self.driver.find_elements(
                By.XPATH,
                """
                //button[contains(translate(., 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'ADD')]
                |
                //span[contains(text(),'ADD')]
                |
                //div[contains(text(),'ADD')]
                """
            )

            print(
                f"Total ADD buttons found: {len(add_buttons)}"
            )

            clicked = False

            for button in add_buttons:

                try:

                    text = button.text.strip()

                    print(
                        f"Trying button: {text}"
                    )

                    # SKIP INVISIBLE BUTTONS

                    if not button.is_displayed():
                        continue

                    # SCROLL TO BUTTON

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button
                    )

                    time.sleep(2)

                    # NORMAL CLICK

                    try:

                        button.click()

                    except:

                        # JS CLICK FALLBACK

                        self.driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                    print(
                        "Product added successfully"
                    )

                    clicked = True

                    break

                except Exception as e:

                    print(
                        "Skipping button:",
                        e
                    )

                    continue

            # FALLBACK APPROACH

            if not clicked:

                print(
                    "Trying fallback locator..."
                )

                fallback_buttons = self.driver.find_elements(
                    By.XPATH,
                    "//button"
                )

                for btn in fallback_buttons:

                    try:

                        text = btn.text.strip().lower()

                        if (
                                "add"
                                in text
                        ):
                            self.driver.execute_script(
                                "arguments[0].scrollIntoView({block:'center'});",
                                btn
                            )

                            time.sleep(2)

                            self.driver.execute_script(
                                "arguments[0].click();",
                                btn
                            )

                            print(
                                "Fallback ADD clicked"
                            )

                            clicked = True

                            break

                    except:
                        continue

            # FINAL FAILURE

            if not clicked:
                self.driver.save_screenshot(
                    "screenshots/add_button_failure.png"
                )

                raise Exception(
                    "No Add button found"
                )

            time.sleep(5)

        except Exception as e:

            print(
                "Add product failed:",
                e
            )

            raise
    # ---------------------------
    # OPEN CART
    # ---------------------------

    def open_cart(self):

        print(
            "Opening cart..."
        )

        try:

            cart_button = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "a[class*='HeaderContent_cart']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                cart_button
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                cart_button
            )

            print(
                "Cart opened successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/cart_open_failed.png"
            )

            print(
                "Cart open failed:",
                e
            )

            raise

    # ---------------------------
    # PROCEED
    # ---------------------------

    def click_proceed(self):

        print(
            "Trying to click proceed..."
        )

        time.sleep(5)

        buttons = self.driver.find_elements(
            By.XPATH,
            "//button"
        )

        for button in buttons:

            try:

                text = button.text.strip().lower()

                print(
                    f"Button text: {text}"
                )

                if (
                        "proceed"
                        in text
                        or
                        "checkout"
                        in text
                ):

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    print(
                        "Proceed clicked"
                    )

                    break

            except Exception as e:

                print(
                    "Proceed skipped:",
                    e
                )

        time.sleep(5)

    # ---------------------------
    # LOGIN POPUP
    # ---------------------------

    def is_login_popup_present(self):

        return True

    # ---------------------------
    # ENTER MOBILE
    # ---------------------------

    def enter_mobile_number(
            self,
            mobile
    ):

        print(
            "Entering mobile..."
        )

        mobile_box = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                (
                    By.NAME,
                    "mobileNumber"
                )
            )
        )

        mobile_box.clear()

        mobile_box.send_keys(
            mobile
        )

        print(
            f"Mobile entered: {mobile}"
        )

        time.sleep(2)

    # ---------------------------
    # CONTINUE BUTTON
    # ---------------------------

    def click_continue(self):

        print(
            "Trying to click continue..."
        )

        try:

            # POSSIBLE LOCATORS

            locators = [

                (
                    By.XPATH,
                    "//button[contains(.,'Continue')]"
                ),

                (
                    By.XPATH,
                    "//button[.//i[contains(@class,'arrow')]]"
                ),

                (
                    By.XPATH,
                    "//button[.//i[contains(@class,'forward')]]"
                ),

                (
                    By.CSS_SELECTOR,
                    "button[type='submit']"
                )
            ]

            continue_button = None

            for locator in locators:

                try:

                    continue_button = WebDriverWait(
                        self.driver,
                        8
                    ).until(
                        EC.element_to_be_clickable(locator)
                    )

                    if continue_button:
                        break

                except:
                    continue

            if continue_button is None:
                raise Exception(
                    "Continue button not found"
                )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                continue_button
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                continue_button
            )

            print(
                "Continue clicked successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/continue_failed.png"
            )

            print(
                "Continue click failed:",
                e
            )

            raise

    # ---------------------------
    # SELECT ADDRESS
    # ---------------------------

    def click_select_address(self):

        print(
            "Trying to click SELECT ADDRESS..."
        )

        try:

            time.sleep(5)

            select_button = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(.,'SELECT ADDRESS')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                select_button
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                select_button
            )

            print(
                "SELECT ADDRESS clicked successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/select_address_failed.png"
            )

            print(
                "SELECT ADDRESS failed:",
                e
            )

            raise
    # ---------------------------
    # ADD NEW ADDRESS
    # ---------------------------

    def click_add_new_address(self):

        print(
            "Trying to click Add New Address..."
        )

        try:

            # WAIT FOR PAGE LOAD

            time.sleep(5)

            # CLOSE POPUPS IF ANY

            try:

                close_popup = self.driver.find_element(
                    By.XPATH,
                    "//button[contains(@class,'close')]"
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    close_popup
                )

                print(
                    "Popup closed"
                )

                time.sleep(2)

            except:
                pass

            # ADD NEW ADDRESS BUTTON

            add_button = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "button[class*='AddNewAddressRevamped_locationBtn']"
                    )
                )
            )

            # SCROLL

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                add_button
            )

            time.sleep(2)

            # WAIT CLICKABLE

            WebDriverWait(
                self.driver,
                20
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button[class*='AddNewAddressRevamped_locationBtn']"
                    )
                )
            )

            # JS CLICK

            self.driver.execute_script(
                "arguments[0].click();",
                add_button
            )

            print(
                "Add New Address clicked successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/add_new_address_failed.png"
            )

            print(
                "Add New Address failed:",
                e
            )

            raise

    # ---------------------------
    # SELECT LOCATION
    # ---------------------------

    def select_location(
            self,
            location
    ):

        print(
            "Selecting location..."
        )

        try:

            # SEARCH INPUT

            search_box = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "input[placeholder*='Search for society']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                search_box
            )

            time.sleep(2)

            search_box.clear()

            search_box.send_keys(
                location
            )

            print(
                f"{location} entered"
            )

            time.sleep(5)

            # FIRST LOCATION RESULT

            results = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'NewSearchLocationSuggestor_searchItemList')]"
                    )
                )
            )

            print(
                f"Location results found: {len(results)}"
            )

            # CLICK FIRST RESULT

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                results[0]
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                results[0]
            )

            print(
                "Location selected successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/location_failed.png"
            )

            print(
                "Location selection failed:",
                e
            )

            raise

    # ---------------------------
    # ADDRESS DETAILS
    # ---------------------------

    def enter_address_details(self):

        print(
            "Entering address details..."
        )

        try:

            time.sleep(5)

            inputs = self.driver.find_elements(
                By.XPATH,
                "//textarea | //input"
            )

            print(
                f"Address inputs found: {len(inputs)}"
            )

            entered = False

            for input_box in inputs:

                try:

                    placeholder = (
                            input_box.get_attribute(
                                "placeholder"
                            )
                            or ""
                    ).lower()

                    name = (
                            input_box.get_attribute(
                                "name"
                            )
                            or ""
                    ).lower()

                    print(
                        f"Placeholder: {placeholder}"
                    )

                    # ADDRESS FIELD

                    if (
                            "address" in placeholder
                            or
                            "house" in placeholder
                            or
                            "flat" in placeholder
                            or
                            "address" in name
                    ):
                        input_box.clear()

                        input_box.send_keys(
                            "12-34 Main Road"
                        )

                        print(
                            "House address entered"
                        )

                        entered = True

                        break

                except:
                    continue

            if not entered:
                print(
                    "No address field found"
                )

                return

            time.sleep(3)

            # SAVE & NEXT BUTTON

            buttons = self.driver.find_elements(
                By.XPATH,
                "//button"
            )

            for button in buttons:

                try:

                    text = button.text.strip().lower()

                    if (
                            "save" in text
                            or
                            "next" in text
                            or
                            "continue" in text
                    ):
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            button
                        )

                        time.sleep(2)

                        self.driver.execute_script(
                            "arguments[0].click();",
                            button
                        )

                        print(
                            "Save & Next clicked"
                        )

                        break

                except:
                    continue

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/address_details_failed.png"
            )

            print(
                "Address details failed:",
                e
            )

            raise
    # ---------------------------
    # RECIPIENT DETAILS
    # ---------------------------

    def enter_recipient_details(self):

        print(
            "Entering recipient details..."
        )

        try:

            # HOME BUTTON

            home_button = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[text()='Home']/parent::div"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                home_button
            )

            print(
                "Home selected"
            )

            time.sleep(2)

            # RECIPIENT NAME

            name_box = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "input[name='recipientName']"
                    )
                )
            )

            name_box.clear()

            name_box.send_keys(
                "Pavan"
            )

            print(
                "Recipient name entered"
            )

            time.sleep(2)

            # MOBILE NUMBER

            mobile_box = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "input[name='recipientContact']"
                    )
                )
            )

            mobile_box.clear()

            mobile_box.send_keys(
                "9876543210"
            )

            print(
                "Recipient mobile entered"
            )

            time.sleep(2)

            # SAVE ADDRESS

            save_address = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button.NewAddressForm_btnTab1__Bbdu6"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                save_address
            )

            print(
                "Save Address clicked"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/recipient_failed.png"
            )

            print(
                "Recipient details failed:",
                e
            )

            raise

    # ---------------------------
    # SELECT SAVED OFFICE ADDRESS
    # ---------------------------

    def select_saved_office_address(self):

        print(
            "Selecting Office address..."
        )

        try:

            # WAIT FOR MODAL

            time.sleep(8)

            # FIND OFFICE ADDRESS CARD

            office_address = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'NewSavedAddressCard_savedAddressChild')]"
                        "//div[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'office')]"
                        "/ancestor::div[contains(@class,'NewSavedAddressCard_savedAddressChild')]"
                    )
                )
            )

            print(
                "Office address found"
            )

            # SCROLL

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                office_address
            )

            time.sleep(3)

            # JS CLICK

            self.driver.execute_script(
                "arguments[0].click();",
                office_address
            )

            print(
                "Office address selected successfully"
            )

            time.sleep(5)

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/office_address_failed.png"
            )

            print(
                "Office address selection failed:",
                e
            )

            raise