class DeterministicRuleEngine:
    def enforce_guardrails(self, obj: dict) -> dict:
        payload = obj.get("payload", {})

        if obj["event_type"] in ["PAYMENT", "CREDIT"]:
            amount = payload.get("amount", 0)

            if amount > 5000:
                obj["state"] = "FAILED"
                obj["compliance_flags"].append("VELOCITY_BLOCK")
                return obj

        obj["state"] = "EXECUTED"
        return obj

