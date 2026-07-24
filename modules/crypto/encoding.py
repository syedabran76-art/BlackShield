import base64

from utils.helpers import separator


def encoder():
    while True:
        separator()
        print("BlackShield - Base64 Tools")
        separator()

        print("[1] Encode Text")
        print("[2] Decode Text")
        print("[0] Back")

        choice = input("\nSelect an option: ").strip()

        if choice == "0":
            return

        elif choice == "1":
            text = input("\nEnter text: ")

            encoded = base64.b64encode(
                text.encode("utf-8")
            ).decode("utf-8")

            separator()
            print("Encoded Text:\n")
            print(encoded)
            separator()

            input("\nPress Enter to continue...")

        elif choice == "2":
            text = input("\nEnter Base64 text: ")

            try:
                decoded = base64.b64decode(
                    text.encode("utf-8")
                ).decode("utf-8")

                separator()
                print("Decoded Text:\n")
                print(decoded)
                separator()

            except Exception:
                print("\nInvalid Base64 input.")

            input("\nPress Enter to continue...")

        else:
            print("\nInvalid option.")
