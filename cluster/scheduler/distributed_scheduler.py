import queue
import threading

class DistributedScheduler:

    def __init__(self):
        self.job_queue = queue.Queue()

    def submit_job(self, job):

        self.job_queue.put(job)

        print("[SCHEDULER] Job submitted")

    def start(self):

        threading.Thread(
            target=self.run,
            daemon=True
        ).start()

    def run(self):

        while True:

            job = self.job_queue.get()

            try:

                print("[SCHEDULER] Executing job")

                # ----------------------------------------
                # SUPPORT BOTH:
                # 1. callable functions
                # 2. Job objects with execute()
                # ----------------------------------------

                if callable(job):
                    job()

                elif hasattr(job, "execute"):
                    job.execute()

                else:
                    print("[SCHEDULER ERROR] Unsupported job type")

            except Exception as e:

                print(f"[SCHEDULER ERROR] {e}")
