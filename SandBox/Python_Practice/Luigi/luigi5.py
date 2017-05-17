import luigi
class A(luigi.Task):
    def output(self):
        return luigi.LocalTarget('outputs_for_luigi/luigi5.txt')

    def run(self):
        with self.output().open('w') as fh:
            fh.write('This is Luigi5 testing')

class B(luigi.Task):
    def run(self):
        import pdb;pdb.set_trace()
        other_task = yield A()
        with other_task.open():
            print "This is testing"
        



