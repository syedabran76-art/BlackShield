from core.module_info import show_modules

NAME = "Registry"
VERSION = "1.0.0"
DESCRIPTION = "View installed BlackShield modules."
AUTHOR = "BlackShield Team"


def register(menu):

    def registry():

        print("\nModule information requires loader access.")
        print("Registry system initialized.")

        input(
            "\nPress Enter to continue..."
        )


    menu.register(
        "Module Registry",
        registry
    )
