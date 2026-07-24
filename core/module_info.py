def get_module_info(loader):

    modules = []

    for module in loader.module_info():

        modules.append({
            "name": module.get("name", "Unknown"),
            "version": module.get("version", "1.0.0"),
            "author": module.get("author", "Unknown"),
            "description": module.get(
                "description",
                "No description"
            )
        })

    return modules


def show_modules(loader):

    print("\n" + "=" * 60)
    print("BlackShield Module Registry")
    print("=" * 60)

    for module in get_module_info(loader):

        print(f"""
Name        : {module['name']}
Version     : {module['version']}
Author      : {module['author']}
Description : {module['description']}
""")

        print("-" * 60)
