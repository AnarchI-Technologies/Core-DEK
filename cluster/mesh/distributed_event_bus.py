import asyncio

class DistributedEventBus:
    def __init__(self):
        self.topics = {}

    async def publish(self, topic, data):
        if topic not in self.topics:
            return

        for callback in self.topics[topic]:
            await callback(data)

    def subscribe(self, topic, callback):
        if topic not in self.topics:
            self.topics[topic] = []

        self.topics[topic].append(callback)

        print(f"[EVENT BUS] Subscriber attached to topic: {topic}")
