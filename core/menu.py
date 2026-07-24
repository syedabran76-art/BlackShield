class Menu:

    def __init__(self):

        self.options = []


    def register(self, name, callback):

        self.options.append(
            {
                "name": name,
                "callback": callback
            }
        )


    def run(self):

        while True:

            print("\n" + "=" * 60)
            print("BlackShield Menu")
            print("=" * 60)


            for index, option in enumerate(self.options, 1):

                print(
                    f"[{index}] {option['name']}"
                )


            print("[0] Back")


            choice = input(
                "\nSelect an option: "
            )


            if choice == "0":

                break


            if choice.isdigit():

                index = int(choice) - 1


                if 0 <= index < len(self.options):

                    self.options[index]["callback"]()


                else:

                    print(
                        "Invalid option."
                    )


            else:

                print(
                    "Invalid input."
                )
