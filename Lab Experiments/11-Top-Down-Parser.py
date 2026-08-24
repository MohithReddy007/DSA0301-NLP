grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def parse(symbol, tokens, pos=0):
    if symbol not in grammar:
        return [(symbol, pos + 1)] if pos < len(tokens) and tokens[pos] == symbol else []

    results = []
    for production in grammar[symbol]:
        states = [([], pos)]
        for sym in production:
            new_states = []
            for tree, p in states:
                for subtree, new_p in parse(sym, tokens, p):
                    new_states.append((tree + [subtree], new_p))
            states = new_states
        for tree, p in states:
            results.append(((symbol, tree), p))
    return results

sentence = "the cat sees the dog".split()
results = parse("S", sentence)
print("Accepted:", any(pos == len(sentence) for _, pos in results))
