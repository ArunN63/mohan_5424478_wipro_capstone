import logging
import os


def setup_logger():

    # CREATE LOG FOLDER

    log_folder = "logs"

    os.makedirs(
        log_folder,
        exist_ok=True
    )

    log_file = os.path.join(
        log_folder,
        "test_execution.log"
    )

    # LOGGER

    logger = logging.getLogger()

    logger.setLevel(
        logging.INFO
    )

    # REMOVE OLD HANDLERS

    if logger.hasHandlers():
        logger.handlers.clear()

    # FORMAT

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # FILE HANDLER

    file_handler = logging.FileHandler(
        log_file,
        mode="a",
        encoding="utf-8"
    )

    file_handler.setFormatter(
        formatter
    )

    # CONSOLE HANDLER

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    # ADD HANDLERS

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )

    return logger