import os
import importlib


PLUGIN_DIR = "plugins"


class PluginManager:

    def __init__(self):
        self.plugins = []

    def discover(self):

        if not os.path.exists(PLUGIN_DIR):
            return

        for name in os.listdir(PLUGIN_DIR):

            path = os.path.join(
                PLUGIN_DIR,
                name
            )

            if (
                os.path.isdir(path)
                and os.path.exists(
                    os.path.join(path, "plugin.py")
                )
            ):
                self.plugins.append(name)


    def load(self):

        loaded = []

        for plugin in self.plugins:

            try:
                module = importlib.import_module(
                    f"{PLUGIN_DIR}.{plugin}.plugin"
                )

                loaded.append(module)

            except Exception as e:
                print(
                    f"[!] Failed loading {plugin}: {e}"
                )

        return loaded
