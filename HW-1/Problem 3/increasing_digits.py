def increasing_digits(n):
    """ Returns the number of integers from 1 to $n$ (inclusive) 
    that have all digits in increasing order, where $n$ is
    given as a parameter. 
    """
    count = 0
    for i in range(1, n+1):
        if len(str(i)) == 1:
            count += 1
        else:
            for j in range(len(str(i)) - 1):
                if str(i)[j] < str(i)[j + 1]:
                    count += 1
    return count
    raise NotImplementedError()
