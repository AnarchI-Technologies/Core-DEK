import datetime
import uuid

class UniversalTransactionStateMachine:
    def __init__(self):
        self.allowed_types = ["PAYMENT", "MESSAGE", "ACTION", "CREDIT", "TASK"]

    def normalize_to_state_object(self, tenant_id: str, event_type: str, raw_payload: dict) -> dict:
        if event_type not in self.allowed_types:
            raise ValueError("Unknown event type")

        return {
            "event_id": f"evt_{uuid.uuid4().hex[:12]}",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "tenant_id": tenant_id,
            "event_type": event_type,
            "state": "PENDING",
            "ai_route": "UNASSIGNED",
            "deterministic_fallback": True,
            "compliance_flags": ["UNVERIFIED"],
            "payload": raw_payload
        }

