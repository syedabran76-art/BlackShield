import importlib

from core.loader import ModuleLoader


def main():

    print("=" * 60)
    print("BlackShield Module Test")
    print("=" * 60)


    loader = ModuleLoader()

    loader.discover()


    print("\nTesting modules...\n")


    failed = 0


    for module_name in loader.modules:

        try:

            module = importlib.import_module(
                f"modules.{module_name}.module"
            )


            if hasattr(module, "register"):

                print(
                    f"[✓] {module.NAME}"
                )

            else:

                print(
                    f"[X] {module_name}: Missing register()"
                )

                failed += 1


        except Exception as e:

            print(
                f"[X] {module_name}"
            )

            print(
                f"    Error: {e}"
            )

            failed += 1



    print("\n" + "=" * 60)


    if failed == 0:

        print(
            "All modules loaded successfully."
        )

    else:

        print(
            f"{failed} module(s) failed."
        )


if __name__ == "__main__":
    main()
