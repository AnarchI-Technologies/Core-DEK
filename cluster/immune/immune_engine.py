import random

class ImmuneSystem:
    def inspect_packet(self, packet):
        anomaly_score = random.randint(1, 100)

        if anomaly_score > 90:
            print("[IMMUNE] Potential anomaly detected")
            return False

        return True
