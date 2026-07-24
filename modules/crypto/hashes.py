import hashlib

from utils.helpers import separator


ALGORITHMS = {
    "1": ("MD5", hashlib.md5),
    "2": ("SHA1", hashlib.sha1),
    "3": ("SHA256", hashlib.sha256),
    "4": ("SHA512", hashlib.sha512),
}


def hash_generator():
    separator()
    print("BlackShield - Hash Generator")
    separator()

    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[4] SHA512")
    print("[0] Back")

    choice = input("\nSelect Algorithm: ").strip()

    if choice == "0":
        return

    if choice not in ALGORITHMS:
        print("\nInvalid option.")
        input("\nPress Enter to continue...")
        return

    text = input("\nEnter text: ")

    name, algorithm = ALGORITHMS[choice]

    digest = algorithm(text.encode()).hexdigest()

    separator()
    print(f"Algorithm : {name}")
    print(f"Hash       : {digest}")
    separator()

    input("\nPress Enter to continue...")
