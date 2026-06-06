class NodeElectionEngine:
    def elect_cluster_leader(self, nodes):
        online_nodes = [
            n for n in nodes
            if nodes[n]["status"] == "ONLINE"
        ]

        if not online_nodes:
            return None

        leader = sorted(online_nodes)[0]

        print(f"[ELECTION] Cluster leader elected: {leader}")

        return leader
