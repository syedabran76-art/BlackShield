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

from core.loader import ModuleLoader


def main():

    print("=" * 60)
    print("BlackShield Runtime Test")
    print("=" * 60)

    loader = ModuleLoader()
    loader.discover()

    failed = 0

    print("\nChecking module registration...\n")


    class DummyMenu:

        def __init__(self):
            self.items = []


        def register(self, name, callback):

            self.items.append(name)



    for module_name in loader.modules:

        try:

            import importlib

            module = importlib.import_module(
                f"modules.{module_name}.module"
            )

            menu = DummyMenu()

            module.register(menu)


            print(
                f"[✓] {module.NAME} "
                f"- {len(menu.items)} tools"
            )


        except Exception as e:

            print(
                f"[X] {module_name}"
            )

            print(
                f"    {e}"
            )

            failed += 1


    print("\n" + "=" * 60)


    if failed == 0:

        print(
            "Runtime Status: PERFECT"
        )

    else:

        print(
            f"Runtime Issues: {failed}"
        )


if __name__ == "__main__":
    main()
