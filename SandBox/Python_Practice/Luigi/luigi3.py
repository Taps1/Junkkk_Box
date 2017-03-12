import luigi
import datetime

class DailyReport(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())
    #date = luigi.DateParameter(significant=False)

    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/luigi3.txt")

    def run(self):
        with self.output().open('w') as f:
            f.write("The date is: {}".format(str(self.date)))
