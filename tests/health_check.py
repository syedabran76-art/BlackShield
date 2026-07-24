import os


REQUIRED_PATHS = [
    "main.py",

    "core",
    "core/loader.py",
    "core/menu.py",
    "core/logger.py",
    "core/plugin_manager.py",

    "database",
    "database/db.py",
    "database/init_db.py",

    "services/history.py",

    "modules/system",
    "modules/network",
    "modules/crypto",
    "modules/password",
    "modules/filetools",
    "modules/history",
    "modules/reports",
    "modules/settings"
]


def run_check():

    print("=" * 60)
    print("BlackShield Health Check")
    print("=" * 60)


    failed = 0


    for path in REQUIRED_PATHS:

        if os.path.exists(path):

            print(
                f"[✓] {path}"
            )

        else:

            print(
                f"[X] Missing: {path}"
            )

            failed += 1


    print("=" * 60)


    if failed == 0:

        print(
            "System Status: HEALTHY"
        )

    else:

        print(
            f"System Status: {failed} issue(s) found"
        )


if __name__ == "__main__":
    run_check()
