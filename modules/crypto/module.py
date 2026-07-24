NAME = "Cryptography"
VERSION = "1.0.0"
DESCRIPTION = "Hashing and encoding tools."
AUTHOR = "BlackShield Team"


def register(menu):

    from .hashes import hash_generator
    from .encoding import encoder

    menu.register(
        "Hash Generator",
        hash_generator
    )

    menu.register(
        "Base64 Tools",
        encoder
    )
