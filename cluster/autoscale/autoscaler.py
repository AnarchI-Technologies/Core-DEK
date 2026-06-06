class AutoScaler:
    def evaluate_cluster_load(self, workload):
        if workload > 75:
            print("[AUTOSCALER] High load detected")
            print("[AUTOSCALER] Scaling cluster horizontally")

        elif workload < 20:
            print("[AUTOSCALER] Low load detected")
            print("[AUTOSCALER] Scaling cluster down")
