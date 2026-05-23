import os

from datetime import datetime

import allure


def take_screenshot(driver, name):

    # CREATE FOLDER

    if not os.path.exists(
            "screenshots"
    ):

        os.makedirs(
            "screenshots"
        )

    # TIMESTAMP

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    # FILE PATH

    file_path = (
        f"screenshots/{name}_{timestamp}.png"
    )

    # SAVE SCREENSHOT

    driver.save_screenshot(
        file_path
    )

    print(
        f"Screenshot saved: {file_path}"
    )

    # ATTACH TO ALLURE

    with open(
            file_path,
            "rb"
    ) as image_file:

        allure.attach(
            image_file.read(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )