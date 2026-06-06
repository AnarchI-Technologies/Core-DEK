import time

class FailoverEngine:
    def __init__(self, registry, timeout=15):
        self.registry = registry
        self.timeout = timeout

    def inspect_cluster_health(self):
        current = time.time()

        for node_id, node in self.registry.nodes.items():
            delta = current - node["last_heartbeat"]

            if delta > self.timeout:
                node["status"] = "OFFLINE"

                print(f"[FAILOVER] Node failure detected: {node_id}")
                print("[FAILOVER] Triggering workload redistribution")
