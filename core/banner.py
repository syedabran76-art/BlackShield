import os

from core.version import VERSION
from core.theme import show_theme


def show_banner():

    banner_file = "assets/banner.txt"


    if os.path.exists(banner_file):

        with open(
            banner_file,
            "r",
            encoding="utf-8"
        ) as file:

            print(
                file.read()
            )

    else:

        print(
            "BlackShield Cybersecurity Toolkit"
        )


    print(
        f"Version: {VERSION}"
    )

    show_theme()

    print(
        "=" * 60
    )
