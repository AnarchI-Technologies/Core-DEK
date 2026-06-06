from dek.runtime.state_store import load_state

def get_cluster_snapshot():
    return load_state()
