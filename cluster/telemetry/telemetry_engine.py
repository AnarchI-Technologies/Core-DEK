import time

class ClusterTelemetry:
    def emit_metric(self, metric, value):
        print(f"[TELEMETRY] {metric} = {value} @ {time.time()}")
