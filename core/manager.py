from core.menu import Menu


class MenuManager:

    def __init__(self):

        self.categories = {}

    def create_category(self, name):

        menu = Menu(name)

        self.categories[name] = menu

        return menu

    def get(self, name):

        return self.categories.get(name)

    def categories_menu(self):

        while True:

            print("\n" + "=" * 60)
            print("BlackShield")
            print("=" * 60)

            names = list(self.categories.keys())

            for index, name in enumerate(names, start=1):
                print(f"[{index}] {name}")

            print("[0] Exit")

            choice = input("\nSelect Category: ").strip()

            if choice == "0":
                break

            if not choice.isdigit():
                print("Invalid input.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(names):

                self.categories[names[choice - 1]].run()

            else:
                print("Invalid option.")
