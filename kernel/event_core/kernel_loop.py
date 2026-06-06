import time

class KernelLoop:
    def __init__(self, orchestrator, replay_engine):
        self.orchestrator = orchestrator
        self.replay = replay_engine

    def tick(self, event):
        self.orchestrator.health_scan()
        result = self.orchestrator.assign(event)

        if result:
            self.replay.record(event, result)

        return result

    def run_forever(self, event_stream):
        for event in event_stream:
            self.tick(event)
            time.sleep(0.1)

