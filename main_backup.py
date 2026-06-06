from cluster.registry.node_registry import NodeRegistry
from cluster.heartbeat.heartbeat_engine import HeartbeatEngine
from cluster.orchestrator.orchestrator import ClusterOrchestrator

from cluster.transport.transport_engine import ClusterTransport
from cluster.scheduler.distributed_scheduler import DistributedScheduler
from cluster.state.distributed_state import DistributedStateManager
from cluster.recovery.recovery_engine import RecoveryEngine
from cluster.consensus.consensus_engine import ConsensusEngine

import threading
import time

registry = NodeRegistry()

nodeA = registry.register_node("alpha")
nodeB = registry.register_node("beta")

heartbeat = HeartbeatEngine(registry)

heartbeat.start_heartbeat(nodeA["id"])
heartbeat.start_heartbeat(nodeB["id"])

orchestrator = ClusterOrchestrator(registry)

leader = orchestrator.elect_leader()

print(f"[BOOTSTRAP] Cluster leader: {leader}")

# ============================================================
# TRANSPORT
# ============================================================

transport = ClusterTransport(port=9100)

threading.Thread(
    target=transport.start_listener,
    daemon=True
).start()

# ============================================================
# DISTRIBUTED STATE
# ============================================================

state_manager = DistributedStateManager()

state_manager.update_state(
    "cluster_status",
    "ACTIVE"
)

# ============================================================
# SCHEDULER
# ============================================================

scheduler = DistributedScheduler()

scheduler.start()

scheduler.submit_job(
    lambda: print("[JOB] Distributed task executed")
)

# ============================================================
# CONSENSUS
# ============================================================

consensus = ConsensusEngine()

consensus.validate_cluster_state([
    {"status": "ACTIVE"},
    {"status": "ACTIVE"}
])

# ============================================================
# RECOVERY ENGINE
# ============================================================

recovery = RecoveryEngine()

threading.Thread(
    target=recovery.attempt_recovery,
    daemon=True
).start()

# ============================================================
# MAIN LOOP
# ============================================================

print("")
print("===================================================")
print(" LUMENCORE DISTRIBUTED EVENT KERNEL ACTIVE ")
print("===================================================")
print("")

while True:
    time.sleep(1)
