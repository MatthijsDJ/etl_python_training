import pandas as pd
from etl import ETLJob


class CRMETLJob(ETLJob):
    def run(self):
        print('We draaien de crm job')
        self.log('Lees CRM Data')
        self.read('CiviCRM_contact_zoeken.csv')
        self.csv2parquet('CiviCRM_contact_zoeken.csv')

    def read(self, file):
        with open(file, 'r') as f:
            print(f.read())
    
    def csv2parquet(self, file):
        df = pd.read_csv(file)
        df.to_parquet('civi.parquet')