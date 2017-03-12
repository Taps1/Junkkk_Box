import luigi

class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/words.txt")

    def run(self):
        words = ['apple', 'banana', 'grapes']
        with self.output().open('w') as f:
            for word in words:
                f.write("{0}\n".format(word))
        #return "Hello Talat"

class CountLetters(luigi.Task):
    def requires(self):
        for i in range(10):
           return GenerateWords()

    def output(self):
        return luigi.LocalTarget("outputs_for_luigi/letter_counts.txt")

    def run(self):
        with self.input().open('r') as infile:
            words = infile.read().splitlines()

        with self.output().open('w') as outfile:
            for word in words:
                outfile.write('{0} | {1}\n'.format(word, len(word)))

if __name__ == '__main__':
    CountLetters().run()
