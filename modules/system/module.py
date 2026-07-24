NAME = "System"
VERSION = "1.0.0"
DESCRIPTION = "System information utilities."
AUTHOR = "BlackShield Team"


def register(menu):

    from .info import system_info

    menu.register(
        "System Information",
        system_info
    )
