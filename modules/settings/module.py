import json

CONFIG_FILE = "config/config.json"

NAME = "Settings"
VERSION = "1.0.0"
DESCRIPTION = "BlackShield Settings"
AUTHOR = "BlackShield Team"


def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)


def settings():
    while True:

        config = load_config()

        print("\n" + "=" * 60)
        print("BlackShield Settings")
        print("=" * 60)

        print(f"[1] Debug Mode     : {config['debug']}")
        print(f"[2] Logging        : {config['logging']}")
        print(f"[3] Theme          : {config['theme']}")
        print("[0] Back")

        choice = input("\nSelect Option: ").strip()

        if choice == "0":
            return

        elif choice == "1":
            config["debug"] = not config["debug"]

        elif choice == "2":
            config["logging"] = not config["logging"]

        elif choice == "3":
            theme = input("Theme (default/minimal/matrix): ").strip()

            if theme:
                config["theme"] = theme

        else:
            continue

        save_config(config)

        print("\nSettings saved successfully.")


def register(menu):
    menu.register("Settings", settings)
