import pytest
from etl import ETLJob


def test_incremental_job_id():
    """
    setup: id_counter is intieel 0
    als er een nieuwe job wordt aangemaakt
    dan moet de job de job_id hebben met waarde 1
    en nadien moet de id_counter gelijk zijn aan 1
    """
    assert ETLJob.id_counter == 0
    job = ETLJob(name='test job')
    assert job.id == 1
    assert ETLJob.id_counter == 1

def test_priority_setting_in_valid_range():
    """
    Accept priority between 0 and 9
    """
    job = ETLJob(name='test job')
    job.priority = 9
    assert job.priority == 9

def test_priority_setting_in_invalid_range():
    '''
    Raises an ValueError if priority is set to invallid value
    '''
    with pytest.raises(ValueError):
        job = ETLJob(name='test job')
        job.priority = 100
