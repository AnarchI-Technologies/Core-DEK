from cluster.registry.node_registry import DistributedNodeRegistry as NodeRegistry
from cluster.orchestrator.orchestrator import ClusterOrchestrator
from cluster.heartbeat.heartbeat_engine import HeartbeatEngine

from cluster.scheduler.distributed_scheduler import DistributedScheduler
from cluster.state.distributed_state import DistributedStateManager
from cluster.consensus.consensus_engine import ConsensusEngine
from cluster.transport.transport_engine import ClusterTransport
from cluster.recovery.recovery_engine import RecoveryEngine

import threading
import time

# =========================
# BOOT SYSTEM
# =========================

registry = NodeRegistry()

nodeA = registry.register_node("alpha", "worker")
nodeB = registry.register_node("beta", "worker")

heartbeat = HeartbeatEngine(registry)

heartbeat.start_heartbeat(nodeA)
heartbeat.start_heartbeat(nodeB)

orchestrator = ClusterOrchestrator()
orchestrator.nodes = registry.get_cluster_state()

state_manager = DistributedStateManager()
state_manager.update_state("cluster_status", "ACTIVE")

# =========================
# LEADER ELECTION (CLEAN)
# =========================

leader = orchestrator.elect_leader()

if leader is None:
    leader = nodeA
    print("[ELECTION] Fallback leader assigned:", leader)
else:
    print("[ELECTION] Cluster leader elected:", leader)

state_manager.update_state("leader", leader)

print("[BOOTSTRAP] Cluster leader:", state_manager.get_state("leader"))

# =========================
# SCHEDULER
# =========================

scheduler = DistributedScheduler()
scheduler.start()

def leader_guarded_job():
    current_leader = state_manager.get_state("leader")
    print(f"[SCHEDULER] Running under leader: {current_leader}")
    print("[JOB] Distributed task executed")

scheduler.submit_job(leader_guarded_job)

# =========================
# CONSENSUS
# =========================

consensus = ConsensusEngine()
consensus.validate_cluster_state([
    {"status": "ACTIVE"},
    {"status": "ACTIVE"}
])

# =========================
# TRANSPORT
# =========================

transport = ClusterTransport(port=9100)

threading.Thread(target=transport.start_listener, daemon=True).start()

# =========================
# RECOVERY
# =========================

recovery = RecoveryEngine()

threading.Thread(target=recovery.attempt_recovery, daemon=True).start()

# =========================
# MAIN LOOP
# =========================

print("\n===================================================")
print(" LUMENCORE DISTRIBUTED EVENT KERNEL ACTIVE ")
print("===================================================\n")

while True:
    nodes = registry.get_cluster_state()

    for node_id in nodes.keys():
        heartbeat.start_heartbeat(node_id)

    print("[HEARTBEAT] Cluster alive | Leader=" + str(state_manager.get_state("leader")))

    time.sleep(1)

