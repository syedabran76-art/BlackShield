from core.logger import show_log


NAME = "Logs"
VERSION = "1.0.0"
DESCRIPTION = "View BlackShield logs."
AUTHOR = "BlackShield Team"



def register(menu):

    menu.register(
        "View Logs",
        show_log
    )
