NAME = "Example Plugin"
VERSION = "1.0.0"


def register(menu):

    def hello():
        print("\nHello from Example Plugin!")
        input("\nPress Enter to continue...")

    menu.register(
        "Example Plugin",
        hello
    )
