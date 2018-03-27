def prime_linear_sieve(n):
    is_composite = [False] * (n + 1)
    primes = list()
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
        for j in primes:
            if j * i > n:
                break
            is_composite[j * i] = True
            if i % j == 0:
                break
    return primes


def is_prime_naive(k):
    if k < 2:
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i += 1
        return True
