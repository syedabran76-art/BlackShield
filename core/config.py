import json
import os

CONFIG_FILE = os.path.join("config", "config.json")


def load_config():
    """
    Load the configuration file.
    Returns a dictionary.
    """
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")
    except json.JSONDecodeError:
        raise ValueError("Configuration file contains invalid JSON.")


def save_config(data):
    """
    Save configuration to config.json.
    """
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get(key, default=None):
    """
    Get a configuration value.
    """
    config = load_config()
    return config.get(key, default)


def set(key, value):
    """
    Update a configuration value.
    """
    config = load_config()
    config[key] = value
    save_config(config)
