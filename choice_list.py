def choice_noun():
    while True:
        nouns = list(map(str, input("Write 3 nouns: ").split()))
        if len(nouns) != 3:
            print('I said 3..')
            continue
        else:
            break
    return nouns


def choice_verb():
    while True:
        verbs = list(map(str, input("and 3 verbs, please: ").split()))
        if len(verbs) != 3:
            print('I said 3...')
            continue
        else:
            break
    return verbs


def choice_adj():
    while True:
        adj = list(map(str, input("also 3 adjectives: ").split()))
        if len(adj) != 3:
            print('I said 3...')
            continue
        else:
            break
    return adj