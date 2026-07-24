import os
from datetime import datetime

from utils.helpers import separator


def file_metadata():
    separator()
    print("BlackShield - File Metadata")
    separator()

    path = input("Enter file path: ").strip()

    if not os.path.isfile(path):
        print("\nFile not found.")
        separator()
        input("\nPress Enter to continue...")
        return

    stat = os.stat(path)

    print(f"\nFile Name      : {os.path.basename(path)}")
    print(f"Directory      : {os.path.dirname(path)}")
    print(f"Size           : {stat.st_size} bytes")
    print(f"Extension      : {os.path.splitext(path)[1] or 'None'}")
    print(f"Readable       : {os.access(path, os.R_OK)}")
    print(f"Writable       : {os.access(path, os.W_OK)}")
    print(f"Executable     : {os.access(path, os.X_OK)}")

    print("\nTimestamps")
    print("-" * 60)
    print(f"Modified : {datetime.fromtimestamp(stat.st_mtime)}")
    print(f"Accessed : {datetime.fromtimestamp(stat.st_atime)}")
    print(f"Created  : {datetime.fromtimestamp(stat.st_ctime)}")

    separator()
    input("\nPress Enter to continue...")
