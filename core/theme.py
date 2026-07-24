import json
import os

CONFIG_FILE = "config/config.json"


THEMES = {
    "default": {
        "name": "Default"
    },
    "minimal": {
        "name": "Minimal"
    },
    "matrix": {
        "name": "Matrix"
    }
}


def get_theme():

    if not os.path.exists(CONFIG_FILE):
        return "default"

    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)

    return config.get("theme", "default")


def show_theme():

    theme = get_theme()

    print(f"[Theme] {THEMES.get(theme, THEMES['default'])['name']}")
