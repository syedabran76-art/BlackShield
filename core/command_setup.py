from core.command import CommandManager
from core.aliases import setup_aliases


def setup_commands(menu):

    manager = CommandManager()


    manager.register(
        "menu",
        menu.run,
        "Open menu system"
    )


    manager.register(
        "about",
        lambda: print(
            "BlackShield Cybersecurity Toolkit"
        ),
        "Show information"
    )


    setup_aliases(
        manager,
        menu
    )


    return manager
