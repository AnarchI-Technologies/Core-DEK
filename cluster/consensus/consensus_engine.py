class ConsensusEngine:
    def validate_cluster_state(self, states):
        if not states:
            return False

        # HARD NORMALIZATION LAYER (single contract: "status")
        normalized = []

        for s in states:
            if isinstance(s, dict):
                if "cluster_status" in s:
                    normalized.append(s["cluster_status"])
                elif "status" in s:
                    normalized.append(s["status"])
                elif "state" in s:
                    normalized.append(s["state"])
                else:
                    normalized.append("UNKNOWN")
            else:
                normalized.append(str(s))

        baseline = normalized[0]

        for s in normalized:
            if s != baseline:
                print("[CONSENSUS] State divergence detected:", normalized)
                return False

        print("[CONSENSUS] Cluster state validated")
        return True
