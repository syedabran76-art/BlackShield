NAME = "File Tools"
VERSION = "1.0.0"
DESCRIPTION = "File analysis and integrity tools."
AUTHOR = "BlackShield Team"


def register(menu):

    from .integrity import integrity_checker
    from .metadata import file_metadata

    menu.register(
        "File Integrity Checker",
        integrity_checker
    )

    menu.register(
        "File Metadata",
        file_metadata
    )
