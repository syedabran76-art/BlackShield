import os
import platform
from datetime import datetime


def clear():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """
    Wait for the user to press Enter.
    """
    input("\nPress Enter to continue...")


def current_time():
    """
    Return the current local time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_platform():
    """
    Return the current operating system.
    """
    return platform.system()


def separator(length=60):
    """
    Print a separator line.
    """
    print("=" * length)
