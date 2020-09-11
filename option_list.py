
noun_index = ['_n1_', '_n2_', '_n3_']
verb_index = ['_v1_', '_v2_', '_v3_']
adj_index = ['_a1_', '_a2_', '_a3_']


def loveletter():
    fname = open('loveletter.txt')
    file = fname.read()
    letter = file
    return letter


def friends():
    fname = open('../MadLib2/friends.txt')
    file = fname.read()
    letter = file
    return letter


def replaceletter(letter, nouns, verbs, adj):
    n = 0
    while n < len(nouns):
        for i in noun_index:
            letter = letter.replace(i, nouns[n])
            n += 1
    n = 0
    while n < len(verbs):
        for i in verb_index:
            letter = letter.replace(i, verbs[n])
            n += 1
    n = 0
    while n < len(adj):
        for i in adj_index:
            letter = letter.replace(i, adj[n])
            n += 1

    return letter
