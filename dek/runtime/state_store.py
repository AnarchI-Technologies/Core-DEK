from threading import RLock

_STATE = {
    "nodes": {},
    "leader": None,
    "cluster_status": "INIT"
}

_LOCK = RLock()

def load_state():
    with _LOCK:
        return dict(_STATE)

def save_state(new_state):
    global _STATE
    with _LOCK:
        _STATE = dict(new_state)
