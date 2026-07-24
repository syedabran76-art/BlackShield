import logging
import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(
    LOG_DIR,
    "blackshield.log"
)


os.makedirs(
    LOG_DIR,
    exist_ok=True
)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)


def info(message, module="CORE"):

    logging.info(
        f"[{module}] {message}"
    )


def warning(message, module="CORE"):

    logging.warning(
        f"[{module}] {message}"
    )


def error(message, module="CORE"):

    logging.error(
        f"[{module}] {message}"
    )


def debug(message, module="CORE"):

    logging.debug(
        f"[{module}] {message}"
    )


def show_log():

    print("\nBlackShield Logs")
    print("=" * 60)

    if not os.path.exists(LOG_FILE):
        print("No logs available.")
        return


    with open(
        LOG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        print(
            file.read()
        )
