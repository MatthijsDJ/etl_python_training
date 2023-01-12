from typing_extensions import Self


class ETLPriorityError(Exception):
    pass


"""
Job container for ETL jobs
"""
class ETLJob: # base class
    """
    ETL class
    """
    id_counter = 0

    def __init__(self, name) -> None:
        ETLJob.id_counter += 1
        self.id = ETLJob.id_counter
        self.name = name
        self.failed = False
        self.last_run_timestamp = None
        self.priority = 0

    def get_priority(self) -> int:
        return self._priority

    def set_priority(self, priority) -> Self:
        
        if priority not in range(0,10):
            raise ValueError('priority has to be in range 0 - 9')
        else:
            self._priority = priority
            return self


    def fail(self):
        self.log('Job failed')

    def log(self, message):
        print(f'LOG: {message}')

    def run(self):
        print(f'RUN {self.name} IS ER NOG NIET JA!')

    priority = property(get_priority, set_priority)