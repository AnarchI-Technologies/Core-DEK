import yaml

class ConfigLoader:
    def __init__(self, path="config/dek.yaml"):
        self.path = path
        self.data = {}

    def load(self):
        with open(self.path, "r") as f:
            self.data = yaml.safe_load(f)

        print("[CONFIG] Loaded configuration")

        return self.data
