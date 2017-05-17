import luigi

@luigi.Task.event_handler(luigi.Event.SUCCESS)
def hello(task):
    print "Task has been successfully completed"

class TaskA(luigi.Task):
    priority = 10
    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/TaskA.txt")

    def run(self):
        import pdb;pdb.set_trace()
        words = ['apple1', 'banana1', 'grapes1']
        with self.output().open('w') as f:
            for word in words:
                f.write('{}\n'.format(word))


class TaskB(luigi.Task):
    priority = 100
#    def requires(self):
#        return TaskA()

    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/TaskB.txt")

    def run(self):
        import pdb;pdb.set_trace()
        self.set_tracking_url("http://google.com/")
        words = ['apple1', 'banana1', 'grapes1']
        with self.output().open('w') as f:
            for word in words:
                f.write('{}\n'.format(word+'B'))

class TaskC(luigi.Task):
    def requires(self):
        return [TaskB(), TaskA()]
    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/TaskC.txt")
    
    def run(self):
        import pdb;pdb.set_trace()
        self.set_tracking_url("http://google.com/")
        words = ['apple1', 'banana1', 'grapes1']
        with self.output().open('w') as f:
            for word in words:
                f.write('{}\n'.format(word+'C'))        
