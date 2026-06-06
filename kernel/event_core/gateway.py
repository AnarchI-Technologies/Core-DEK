import uuid

class NexusAPIGateway:
    def __init__(self):
        self.registered_tenants = {
            "tenant_lumencore_gaming_01": {"status": "ACTIVE", "tier": "ENTERPRISE"},
            "tenant_external_operator_02": {"status": "ACTIVE", "tier": "DEVELOPER_API"}
        }

    def process_incoming_request(self, tenant_id: str, secret_key: str, raw_payload: dict) -> dict:
        if secret_key != "NEXUS_SECURE_AUTH_KEY":
            raise PermissionError("401 Unauthorized")

        tenant = self.registered_tenants.get(tenant_id)
        if not tenant:
            raise PermissionError("401 Unknown Tenant")

        if tenant["status"] != "ACTIVE":
            raise ConnectionRefusedError("403 Tenant Disabled")

        return {
            "gateway_ingress_id": f"ingres_{uuid.uuid4().hex[:8]}",
            "validated_tenant_id": tenant_id,
            "forward_payload": raw_payload
        }

