from etl import ETLJob

class LoanETLJob(ETLJob):
    def run(self):
        print(f'We runnen de {self.name} job')
        self.log('Lees data in.')