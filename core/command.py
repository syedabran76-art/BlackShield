class CommandManager:

    def __init__(self):
        self.commands = {}

    def register(self, name, callback, description=""):
        self.commands[name] = {
            "callback": callback,
            "description": description
        }

    def show_help(self):

        print("\nAvailable Commands")
        print("-" * 60)

        for name, data in self.commands.items():
            print(
                f"{name:<15} - {data['description']}"
            )


    def run(self):

        while True:

            command = input(
                "\nBlackShield > "
            ).strip().lower()


            if command == "":
                continue


            if command == "help":
                self.show_help()
                continue


            if command == "exit":
                print("Exiting BlackShield...")
                break


            if command in self.commands:

                try:
                    self.commands[command]["callback"]()

                except Exception as e:
                    print(f"Error: {e}")

            else:
                print(
                    "Unknown command. Type 'help'."
                )
