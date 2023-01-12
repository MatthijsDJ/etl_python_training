from etl import (ETLJobController,
                 ETLJob)

def test_add_job():
    """
        Als er een nieuwe jobrunner wordt aangemaakt
        en je voegt er vervolgens een job aan toe
        dan is daarna de lengte van jobs 1 zijn
    """

    # Setup
    job_controller = ETLJobController()
    job1 = ETLJob('job 1')
    # Run
    job_controller.add_job(job1)
    # Eval
    assert len(job_controller.jobs) == 1
