import importlib


def setup_aliases(command_manager, menu):


    aliases = {

        "crypto": "modules.crypto.module",
        "network": "modules.network.module",
        "system": "modules.system.module",
        "password": "modules.password.module",
        "files": "modules.filetools.module",
        "history": "modules.history.module",
        "reports": "modules.reports.module",
        "settings": "modules.settings.module"

    }


    def open_module(path):

        try:

            module = importlib.import_module(path)


            print(
                f"\nOpening {module.NAME}..."
            )


            temp_menu = []


            class ModuleMenu:

                def register(self, name, callback):

                    temp_menu.append(
                        {
                            "name": name,
                            "callback": callback
                        }
                    )


            module.register(
                ModuleMenu()
            )


            while True:

                print("\n" + "=" * 60)
                print(module.NAME)
                print("=" * 60)


                for i, item in enumerate(temp_menu, 1):

                    print(
                        f"[{i}] {item['name']}"
                    )


                print("[0] Back")


                choice = input(
                    "\nSelect Option: "
                )


                if choice == "0":

                    break


                if choice.isdigit():

                    index = int(choice) - 1


                    if 0 <= index < len(temp_menu):

                        temp_menu[index]["callback"]()


                    else:

                        print(
                            "Invalid option."
                        )


                else:

                    print(
                        "Invalid input."
                    )


        except Exception as e:

            print(
                f"Module error: {e}"
            )



    for command, path in aliases.items():

        command_manager.register(
            command,
            lambda p=path: open_module(p),
            f"Open {command} module"
        )
