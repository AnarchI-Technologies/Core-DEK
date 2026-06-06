class NexusAIRouter:
    def assign_agent_workflow(self, state_object: dict) -> dict:
        e_type = state_object["event_type"]

        if e_type == "MESSAGE":
            state_object["ai_route"] = "Engagement_Agent"
        elif e_type in ["PAYMENT", "CREDIT"]:
            state_object["ai_route"] = "Transaction_Agent"
        else:
            state_object["ai_route"] = "Core_Agent"

        state_object["state"] = "ROUTED"
        return state_object

