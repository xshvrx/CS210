def primes(n):
    """Returns all prime numbers from 2 to n (excluding n) """
    list = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list
    raise NotImplementedError()
