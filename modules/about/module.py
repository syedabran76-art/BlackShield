NAME = "About"
VERSION = "1.0.0"
DESCRIPTION = "BlackShield information."
AUTHOR = "BlackShield Team"


def register(menu):

    def about():

        print("""
BlackShield Framework

A modular cybersecurity learning toolkit.

Developer:
BlackShield Team
""")

        input(
            "\nPress Enter to continue..."
        )


    menu.register(
        "About BlackShield",
        about
    )
