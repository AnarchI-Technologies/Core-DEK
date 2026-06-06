import time

class RecoveryEngine:
    def __init__(self):
        self.failed_nodes = []

    def report_failure(self, node_id):
        self.failed_nodes.append(node_id)

        print(f"[RECOVERY] Failure detected: {node_id}")

    def attempt_recovery(self):
        while True:
            if self.failed_nodes:
                node = self.failed_nodes.pop(0)

                print(f"[RECOVERY] Attempting recovery for {node}")

            time.sleep(5)
