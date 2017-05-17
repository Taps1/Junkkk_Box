import luigi
import datetime
import luigi.contrib.hdfs

class DataDump(luigi.ExternalTask):
    date = luigi.DateParameter()
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget(self.date.strftime('/var/log/dump/%Y-%m-%d.txt'))


class AggregationTask(luigi.Task):
    date = luigi.DateParameter()
    window = luigi.IntParameter()
    def requires(self):
        return [DataDump(self.date - datetime.timedelta(i)) for i in xrange(self.window)]
    def run(self):
        import pdb;pdb.set_trace()
        with self.output().open('w') as fh:
            fh.write("Hello Talat Parwez")
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/aggregated-%s-%d' %(self.date, self.window))


class RunAll(luigi.Task):
    ''' Dummy task that triggers execution of a other tasks'''
    def requires(self):
        for window in [3]:
            for d in xrange(4): # guarantee that aggregations were run for the past 10 days
                yield AggregationTask(datetime.date.today() - datetime.timedelta(d), window)
