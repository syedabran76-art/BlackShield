import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from core.menu import Menu
from core.loader import ModuleLoader
from core.plugin_manager import PluginManager
from core.config import load_config


def main():

    print("=" * 60)
    print("BlackShield Startup Test")
    print("=" * 60)


    errors = 0


    try:

        config = load_config()

        print(
            "[✓] Configuration loaded"
        )


    except Exception as e:

        print(
            "[X] Config error:",
            e
        )

        errors += 1



    try:

        menu = Menu()

        print(
            "[✓] Menu initialized"
        )


    except Exception as e:

        print(
            "[X] Menu error:",
            e
        )

        errors += 1



    try:

        loader = ModuleLoader()

        loader.discover()

        loader.register_modules(menu)


        print(
            f"[✓] Modules loaded: {len(loader.modules)}"
        )


    except Exception as e:

        print(
            "[X] Module error:",
            e
        )

        errors += 1



    try:

        plugins = PluginManager()

        plugins.discover()

        loaded = plugins.load()


        print(
            f"[✓] Plugins loaded: {len(loaded)}"
        )


    except Exception as e:

        print(
            "[X] Plugin error:",
            e
        )

        errors += 1



    print("\n" + "=" * 60)


    if errors == 0:

        print(
            "Startup Status: PERFECT"
        )

    else:

        print(
            f"Startup Issues: {errors}"
        )



if __name__ == "__main__":
    main()
