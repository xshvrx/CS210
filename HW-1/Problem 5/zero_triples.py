def zero_triples(ints):
    """ 
    Returns all triples in a list of integers that sum to zero. 
    The list of integers is given as a parameter. 
    Assumes the list will not contain any duplicates, and a triple 
    should not use the same number more than once.
    """
    triples = []
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            for k in range(j + 1, len(ints)):
                if ints[i] + ints[j] + ints[k] == 0:
                    triples.append([ints[i], ints[j], ints[k]])
    return triples
    raise NotImplementedError()
