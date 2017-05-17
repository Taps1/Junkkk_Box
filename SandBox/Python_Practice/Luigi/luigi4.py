import luigi

class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget('outputs_for_luigi/words.txt')

    def run(self):
        words = ['apple', 'banana', 'grape']
        with self.output().open('w') as f:
            for word in words:
                f.write('{word}\n'.format(word=word))
  
class CountLetters(luigi.Task):
    def requires(self):
        return GenerateWords()

    def output(self):
        return luigi.LocalTarget('outputs_for_luigi/letter_counts.txt')

    def run(self):
        import pdb;pdb.set_trace()
        with self.input().open('r') as infile:
            words = infile.read().splitlines()

        with self.output().open('w') as outfile:
            for word in words:
                outfile.write('{word} | {letter_count}\n'.format(word=word, letter_count=len(word)))
