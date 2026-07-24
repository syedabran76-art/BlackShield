from utils.helpers import separator

NAME = "Help"
VERSION = "1.0.0"
DESCRIPTION = "Help Center"
AUTHOR = "BlackShield Team"


def help_center():
    separator()
    print("BlackShield Help Center")
    separator()

    print("Available Categories\n")

    print("System")
    print("  • System Information")
    print("  • System Monitor\n")

    print("Network")
    print("  • DNS Lookup")
    print("  • IP Information")
    print("  • Ping Host\n")

    print("Cryptography")
    print("  • Hash Generator")
    print("  • Base64 Tools\n")

    print("Password")
    print("  • Password Strength Checker")
    print("  • Secure Password Generator\n")

    print("File Tools")
    print("  • File Integrity Checker")
    print("  • File Metadata\n")

    print("Reports")
    print("  • View Reports\n")

    print("History")
    print("  • View History\n")

    print("About")
    print("  • Project Information")

    separator()
    input("\nPress Enter to continue...")


def register(menu):
    menu.register("Help Center", help_center)
