class WorkerNode:
    def __init__(self, node_id, role="default"):
        self.node_id = node_id
        self.role = role
        self.alive = True

    def execute(self, event):
        return {
            "node": self.node_id,
            "role": self.role,
            "event_id": event.get("id"),
            "status": "processed"
        }

