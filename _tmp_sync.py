from dek.runtime.state_store import load_state, save_state
from cluster.registry.node_registry import DistributedNodeRegistry

def sync_nodes_to_state(registry):
    state = load_state()
    state["nodes"] = registry.get_cluster_state()
    save_state(state)
