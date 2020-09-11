import random

class RandomGen:

    def __init__(self):
        self.nouns = RandomGen.ran_nouns(self)
        self.verbs = RandomGen.ran_verbs(self)
        self.adj = RandomGen.ran_adj(self)

    @staticmethod
    def ran_nouns(self):
        noun_fname = 'nouns.txt'
        fh1 = open(noun_fname)
        nouns = [lines.strip() for lines in fh1]
        ran_nouns = random.sample(nouns, 3)
        fh1.close()
        return ran_nouns

    @staticmethod
    def ran_verbs(self):
        verbs_fname = 'verbs.txt'
        fh2 = open(verbs_fname)
        verbs = [lines.strip() for lines in fh2]
        ran_verbs = random.sample(verbs, 3)
        fh2.close()
        return ran_verbs

    @staticmethod
    def ran_adj(self):
        adj_fname = 'adj.txt'
        fh3 = open(adj_fname)
        adj = [lines.strip() for lines in fh3]
        ran_adj = random.sample(adj, 3)
        fh3.close()
        return ran_adj


