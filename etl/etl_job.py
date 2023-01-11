
class ETLJob: # base class
    def __init__(self, name) -> None:
        self.name = name

    def log(self, message):
        print(f'LOG: {message}')

    def run(self):
        print(f'RUN {self.name} IS ER NOG NIET JA!')

