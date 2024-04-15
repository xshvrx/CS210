def factor(n):
    """Return all the prime factors of n."""
    prime_factors = []
    primes_list = primes(n)
    for prime in primes_list:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n / prime
    if n > 1:
        prime_factors.append(int(n))
    return prime_factors
    raise NotImplementedError()
