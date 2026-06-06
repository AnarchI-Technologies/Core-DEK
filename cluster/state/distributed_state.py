import threading
import copy

class DistributedStateManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.state = {}

    def update_state(self, key, value):
        with self.lock:
            self.state[key] = value

            print(f"[STATE] Updated: {key}")

    def get_state(self, key):
        with self.lock:
            return self.state.get(key)

    def snapshot(self):
        with self.lock:
            return copy.deepcopy(self.state)
