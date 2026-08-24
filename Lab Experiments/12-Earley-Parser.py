grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def earley(tokens):
    chart = [set() for _ in range(len(tokens) + 1)]
    start = ("S'", ("S",), 0, 0)
    chart[0].add(start)

    for i in range(len(tokens) + 1):
        changed = True
        while changed:
            changed = False
            for lhs, rhs, dot, origin in list(chart[i]):
                if dot < len(rhs):
                    sym = rhs[dot]
                    if sym in grammar:
                        for prod in grammar[sym]:
                            item = (sym, tuple(prod), 0, i)
                            if item not in chart[i]:
                                chart[i].add(item)
                                changed = True
                else:
                    for plhs, prhs, pdot, porigin in list(chart[origin]):
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            item = (plhs, prhs, pdot + 1, porigin)
                            if item not in chart[i]:
                                chart[i].add(item)
                                changed = True

        if i < len(tokens):
            for lhs, rhs, dot, origin in list(chart[i]):
                if dot < len(rhs) and rhs[dot] == tokens[i]:
                    chart[i + 1].add((lhs, rhs, dot + 1, origin))

    return ("S'", ("S",), 1, 0) in chart[len(tokens)]

sentence = "the cat sees the dog".split()
print("Accepted:", earley(sentence))
