import src.algolib.number_theory as nt


def is_truncatable(p):
    s = str(p)
    for i in range(1, len(s)):
        if nt.is_prime_naive(int(s[i:])) and nt.is_prime_naive(int(s[:i])):
            continue
        else:
            return False
    return True


def main():
    primes = nt.prime_linear_sieve(1000000)
    truncatable_primes = list()
    for p in primes:
        if p < 10:
            continue
        if is_truncatable(p):
            truncatable_primes.append(p)
    assert len(truncatable_primes) ==11
    print(sum(truncatable_primes))


if __name__ == '__main__':
    main()
