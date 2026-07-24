import time

from core.banner import show_banner
from core.menu import Menu
from core.loader import ModuleLoader
from core.plugin_manager import PluginManager
from core.command_setup import setup_commands
from core.logger import info, error
from core.config import load_config
from utils.helpers import clear


def startup(message, delay=0.15):
    print(f"[*] {message}")
    time.sleep(delay)


def main():

    clear()
    show_banner()

    print("\nBlackShield Framework\n")

    startup("Loading configuration...")
    config = load_config()

    startup("Creating menu...")
    menu = Menu()

    startup("Discovering modules...")
    loader = ModuleLoader()
    loader.discover()
    loader.register_modules(menu)

    startup("Loading plugins...")

    plugin_manager = PluginManager()
    plugin_manager.discover()

    plugins = plugin_manager.load()

    for plugin in plugins:
        if hasattr(plugin, "register"):
            plugin.register(menu)


    startup("Preparing command system...")

    command_manager = setup_commands(menu)


    startup("Framework ready.")


    print("\nLoaded Modules")
    print("-" * 60)

    for module in loader.module_info():

        print(
            f"✓ {module['name']} "
            f"v{module['version']}"
        )


    if plugins:

        print("\nLoaded Plugins")
        print("-" * 60)

        for plugin in plugins:

            print(
                f"✓ {getattr(plugin, 'NAME', 'Unknown')}"
            )


    try:
        command_manager.run()

    except KeyboardInterrupt:

        print("\nExiting BlackShield...")
        info("Shutdown by user.")


    except Exception as e:

        error(str(e))
        print(f"Fatal Error: {e}")


if __name__ == "__main__":
    main()
