class Job:
    def __init__(self, job_id, payload):
        self.job_id = job_id
        self.payload = payload
        self.status = "QUEUED"

    def execute(self):
        self.status = "RUNNING"
        print(f"[JOB] Executing {self.job_id}")
        self.payload()
        self.status = "COMPLETED"
