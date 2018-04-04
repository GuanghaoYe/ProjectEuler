import src.algolib.number_theory as nt

primes = nt.prime_linear_sieve(10000000)


def check(k):
    for prime in primes:
        if prime > k:
            return True
        else:
            remain = k - prime
            if remain % 2 == 1:
                continue
            else:
                remain //= 2
                if remain == int(remain ** 0.5) ** 2:
                    return False


def main():
    for i in range(33, 10000000, 2):
        if i in nt.prime_set:
            continue
        if check(i):
            print(i)
            break


if __name__ == '__main__':
    main()
