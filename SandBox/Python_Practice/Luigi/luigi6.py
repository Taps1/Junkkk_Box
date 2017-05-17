import luigi

class MyTask(luigi.Task):
    def run(self):
        # set tracking URL
        self.set_tracking_url("http://www.google.com/")
        
        for i in range(100):
            if i%10 == 0:
                self.set_status_message("Progress: %d/100"%i)
