NAME = "Network"
VERSION = "1.1.0"
DESCRIPTION = "Networking utilities."
AUTHOR = "BlackShield Team"


def register(menu):

    from .dns import dns_lookup
    from .scanner import port_scanner

    menu.register(
        "DNS Lookup",
        dns_lookup
    )

    menu.register(
        "IP Information",
        port_scanner
    )
