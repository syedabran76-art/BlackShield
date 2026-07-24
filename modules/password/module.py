NAME = "Password"
VERSION = "1.0.0"
DESCRIPTION = "Password security utilities."
AUTHOR = "BlackShield Team"


def register(menu):

    from .checker import password_checker

    menu.register(
        "Password Tools",
        password_checker
    )
