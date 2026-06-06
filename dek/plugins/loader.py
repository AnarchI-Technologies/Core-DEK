import importlib
import pkgutil

class PluginLoader:

    def __init__(self):
        self.plugins = []

    def discover_plugins(self):

        import dek.plugins.builtins as builtin_plugins

        for _, module_name, _ in pkgutil.iter_modules(builtin_plugins.__path__):

            full_name = f"dek.plugins.builtins.{module_name}"

            module = importlib.import_module(full_name)

            self.plugins.append(module)

            print(f"[PLUGIN] Loaded: {module_name}")

    def run_plugins(self):

        for plugin in self.plugins:

            if hasattr(plugin, "run"):

                print(f"[PLUGIN] Executing: {plugin.__name__}")

                plugin.run()
