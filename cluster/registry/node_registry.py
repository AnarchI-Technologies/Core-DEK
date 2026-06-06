import uuid
import time

_GLOBAL_NODES = {}

class DistributedNodeRegistry:
    def __init__(self):
        global _GLOBAL_NODES
        self.nodes = _GLOBAL_NODES

    def register_node(self, node_name, role="worker"):
        node_id = f"node_{uuid.uuid4().hex[:8]}"

        self.nodes[node_id] = {
            "node_name": node_name,
            "role": role,
            "status": "ONLINE",
            "last_heartbeat": time.time()
        }

        print(f"[REGISTRY] Registered node: {node_name}")

        return node_id

    def update_heartbeat(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id]["last_heartbeat"] = time.time()

    def get_cluster_state(self):
        return dict(self.nodes)
