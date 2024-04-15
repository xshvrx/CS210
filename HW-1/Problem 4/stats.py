def stats(ints):
    """ 
    Returns the mean, median, and standard deviation (in that order) of a 
    list of integers given as a parameter. 
    """
    # YOUR CODE HERE
    mean = sum(ints) / len(ints)
    median = 0
    if len(ints) % 2 == 0:
        median = (ints[len(ints) // 2] + ints[len(ints) // 2 - 1]) / 2
    else:
        median = ints[len(ints) // 2]
    std = 0
    for i in ints:
        std += (i - mean) ** 2
    std = math.sqrt(std / (len(ints) - 1))
    return [mean, median, std]
    raise NotImplementedError()
