import hashlib
import os

from utils.helpers import separator


BUFFER_SIZE = 8192


def calculate_hash(path, algorithm="sha256"):
    hasher = hashlib.new(algorithm)

    with open(path, "rb") as file:
        while True:
            chunk = file.read(BUFFER_SIZE)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


def integrity_checker():
    separator()
    print("BlackShield - File Integrity Checker")
    separator()

    path = input("Enter file path: ").strip()

    if not os.path.isfile(path):
        print("\nFile not found.")
        separator()
        input("\nPress Enter to continue...")
        return

    print("\nAlgorithms")
    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")

    choice = input("\nSelect Algorithm: ").strip()

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha512"
    }

    if choice not in algorithms:
        print("\nInvalid option.")
        input("\nPress Enter to continue...")
        return

    digest = calculate_hash(path, algorithms[choice])

    separator()
    print(f"Algorithm : {algorithms[choice].upper()}")
    print(f"Hash      : {digest}")
    separator()

    input("\nPress Enter to continue...")
