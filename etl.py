from simulation import simulation
from main import main


class ETL:
    def source(self, data_source: str):
        if data_source == 'Simulation':
            simulation()
        elif data_source == 'File':
            main()
        return self

    def sink(self, data_sink: str):
        self.data_sink = data_sink
        return self

    def run(self):
        if self.data_sink == 'Console':
            while True:
                simulation()


ETL().source('Simulation').sink('Console').run()
