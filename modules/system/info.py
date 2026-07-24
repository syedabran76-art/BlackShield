import os
import platform
import socket
import shutil
from datetime import datetime

from utils.helpers import separator


def system_info():
    separator()

    print("BlackShield System Information")
    print("-" * 60)

    print(f"Hostname         : {socket.gethostname()}")
    print(f"Operating System : {platform.system()}")
    print(f"Release          : {platform.release()}")
    print(f"Version          : {platform.version()}")
    print(f"Machine          : {platform.machine()}")
    print(f"Processor        : {platform.processor() or 'Unknown'}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Current Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        user = os.getlogin()
    except Exception:
        user = "Unknown"

    print(f"Current User     : {user}")

    print("\nStorage")
    print("-" * 60)

    total, used, free = shutil.disk_usage("/")

    print(f"Total : {total // (1024**3)} GB")
    print(f"Used  : {used // (1024**3)} GB")
    print(f"Free  : {free // (1024**3)} GB")

    separator()

    input("\nPress Enter to continue...")
