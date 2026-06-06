import time
from cluster.workers.node_health import NodeHealth
from cluster.workers.worker_node import WorkerNode

class ClusterOrchestrator:
    def __init__(self):
        self.nodes = {}

    def register_node(self, node_id):
        node = WorkerNode(node_id)
        node.health = NodeHealth()
        self.nodes[node_id] = node

    def heartbeat(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id].health.beat()

    def health_scan(self):
        dead = []

        for node_id, node in self.nodes.items():
            if not node.health.is_alive():
                dead.append(node_id)

        for d in dead:
            print(f"[IMMUNE SYSTEM] Node failure detected: {d}")
            del self.nodes[d]
            self.repair_node(d)

    def repair_node(self, node_id):
        new_id = f"{node_id}_respawn_{int(time.time())}"
        print(f"[IMMUNE SYSTEM] Respawning node: {new_id}")
        self.register_node(new_id)

    def assign(self, event):
        if not self.nodes:
            return None

        node = list(self.nodes.values())[0]
        return node.execute(event)

    def elect_leader(self):
        nodes = list(self.nodes.keys())
        if not nodes:
            return None

        leader_id = nodes[0]
        print(f"[ELECTION] Cluster leader elected: {leader_id}")
        return leader_id
