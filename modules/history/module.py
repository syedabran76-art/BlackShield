NAME = "History"
VERSION = "1.0.0"
DESCRIPTION = "View BlackShield activity history."
AUTHOR = "BlackShield Team"


def register(menu):

    from services.history import get_history

    def history():

        print("\nBlackShield History")

        for row in get_history():

            print(
                f"{row[1]} | {row[2]} | {row[3]}"
            )

        input(
            "\nPress Enter to continue..."
        )


    menu.register(
        "View History",
        history
    )
