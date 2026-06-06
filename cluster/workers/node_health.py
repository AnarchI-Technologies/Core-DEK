import time

class NodeHealth:
    def __init__(self, timeout=10):
        self.last_seen = time.time()
        self.timeout = timeout

    def beat(self):
        self.last_seen = time.time()

    def is_alive(self):
        return (time.time() - self.last_seen) < self.timeout

