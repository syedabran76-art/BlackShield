import importlib
import pkgutil

from core.logger import error


class ModuleLoader:
    def __init__(self, package="modules"):
        self.package = package
        self.modules = {}
        self.failed = {}

    def discover(self):
        package = importlib.import_module(self.package)

        for _, name, ispkg in pkgutil.iter_modules(package.__path__):

            if not ispkg:
                continue

            try:
                module = importlib.import_module(
                    f"{self.package}.{name}.module"
                )

                self.modules[name] = module

            except Exception as e:
                self.failed[name] = str(e)
                error(f"Failed to load module '{name}': {e}")

    def register_modules(self, menu):
        for name, module in self.modules.items():

            try:
                module.register(menu)

            except Exception as e:
                self.failed[name] = str(e)
                error(f"Failed to register '{name}': {e}")

    def module_info(self):
        data = []

        for name, module in self.modules.items():

            data.append({
                "name": getattr(module, "NAME", name),
                "version": getattr(module, "VERSION", "Unknown"),
                "description": getattr(module, "DESCRIPTION", ""),
                "author": getattr(module, "AUTHOR", "Unknown"),
                "status": "Loaded"
            })

        for name, reason in self.failed.items():

            data.append({
                "name": name,
                "version": "-",
                "description": reason,
                "author": "-",
                "status": "Failed"
            })

        return data
