import threading
import time

class HeartbeatEngine:
    def __init__(self, registry, interval=5):
        self.registry = registry
        self.interval = interval

    def start_heartbeat(self, node_id):
        def beat():
            while True:
                self.registry.update_heartbeat(node_id)
                print(f"[HEARTBEAT] Pulse sent from {node_id}")
                time.sleep(self.interval)

        threading.Thread(target=beat, daemon=True).start()
