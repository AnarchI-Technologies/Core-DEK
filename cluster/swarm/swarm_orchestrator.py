class SwarmOrchestrator:
    def redistribute_workload(self, failed_node, active_nodes):
        print(f"[SWARM] Redistributing workload from {failed_node}")

        for node in active_nodes:
            print(f"[SWARM] Migrated tasks to {node}")
