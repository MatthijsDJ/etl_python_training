from .etl_job import ETLJob

class ETLJobController:
    def __init__(self) -> None:
        self.jobs = [] # etl jobs

    def add_job(self, etl_job):
        self.jobs.append(etl_job)

    def run_jobs(self):
        for job in self.jobs:
            job.run()

if __name__ == '__main__':
    job_controller = ETLJobController()
    job1 = ETLJob('job 1')
    job_controller.add_job(job1)
    job2 = ETLJob('job 2')
    job_controller.add_job(job2)

    job_controller.run_jobs()