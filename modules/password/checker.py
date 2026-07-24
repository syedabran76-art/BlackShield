import secrets
import string
import re

from utils.helpers import separator


def password_checker():
    while True:
        separator()
        print("BlackShield - Password Tools")
        separator()

        print("[1] Password Strength Checker")
        print("[2] Secure Password Generator")
        print("[0] Back")

        choice = input("\nSelect an option: ").strip()

        if choice == "0":
            return

        elif choice == "1":
            password = input("\nEnter password: ")

            score = 0
            feedback = []

            if len(password) >= 12:
                score += 1
            else:
                feedback.append("Use at least 12 characters.")

            if re.search(r"[A-Z]", password):
                score += 1
            else:
                feedback.append("Add uppercase letters.")

            if re.search(r"[a-z]", password):
                score += 1
            else:
                feedback.append("Add lowercase letters.")

            if re.search(r"\d", password):
                score += 1
            else:
                feedback.append("Add numbers.")

            if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
                score += 1
            else:
                feedback.append("Add special characters.")

            ratings = {
                0: "Very Weak",
                1: "Weak",
                2: "Fair",
                3: "Good",
                4: "Strong",
                5: "Very Strong"
            }

            separator()
            print(f"Strength : {ratings[score]} ({score}/5)")

            if feedback:
                print("\nSuggestions:")
                for item in feedback:
                    print(f"- {item}")
            else:
                print("\nExcellent password!")

            separator()
            input("\nPress Enter to continue...")

        elif choice == "2":
            try:
                length = int(input("\nPassword Length (12-64): "))
            except ValueError:
                print("Invalid length.")
                continue

            if length < 12 or length > 64:
                print("Length must be between 12 and 64.")
                continue

            alphabet = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

            password = ''.join(
                secrets.choice(alphabet)
                for _ in range(length)
            )

            separator()
            print("Generated Password:\n")
            print(password)
            separator()

            input("\nPress Enter to continue...")

        else:
            print("Invalid option.")
