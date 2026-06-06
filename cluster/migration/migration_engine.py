class WorkloadMigrationEngine:
    def migrate(self, workload_id, source, target):
        print(f"[MIGRATION] Moving {workload_id}")
        print(f"[MIGRATION] {source} -> {target}")
