class ClusterMonitor:
    def inspect(self, nodes):
        for node_id, node in nodes.items():
            print(f"[MONITOR] {node_id} :: {node['status']}")
