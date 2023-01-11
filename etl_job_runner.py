from etl import (ETLJob, ETLJobController)
from loan_etl_job import LoanETLJob
from crm_etl_job import CRMETLJob

def main():
    job_controller = ETLJobController()
    job1 = ETLJob('job 1')
    job_controller.add_job(job1)
    job2 = ETLJob('job 2')
    job_controller.add_job(job2)
    job3 = LoanETLJob('job 3')
    job_controller.add_job(job3)
    job4 = CRMETLJob('job 4')
    job_controller.add_job(job4)
    job_controller.run_jobs()


if __name__ == '__main__':
    main()