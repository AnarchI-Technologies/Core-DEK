import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from examples.demo_run import registry, orchestrator, state_manager

def run_cluster():
    print("[DEK] Booting real cluster runtime...")

    # attach CLI to live system
    nodes = registry.get_cluster_state()

    state_manager.update_state("nodes", nodes)

    print("[DEK] Cluster attached to runtime")


