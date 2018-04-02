import src.algolib.number_theory as nt


def lowest_bit(x):
    return x & (-x)


def get_patterns(p):
    s = str(p)
    length = len(s)
    ret = list()
    for i in range(1, (1 << length) - 1):
        check_str = ''
        pattern = list(s)
        for j in range(0, length):
            if (1 << j) & i:
                check_str += s[j]
                pattern[j] = '*'
        if len(check_str) == 0:
            print(i, p)
        if check_str == check_str[0] * len(check_str):
            ret.append(''.join(pattern))
    return ret


def get_smallest_prime(p):
    for i in range(1, 10):
        s = list(p)
        for j in range(0, len(s)):
            if s[j] == '*':
                s[j] = str(i)
        number = int(''.join(s))
        if nt.is_prime_naive(number):
            return number


def main():
    primes = nt.prime_linear_sieve(1000000)
    pattern_dict = dict()
    for prime in primes:
        patterns = get_patterns(prime)
        for pattern in patterns:
            if pattern not in pattern_dict:
                pattern_dict[pattern] = 1
            else:
                pattern_dict[pattern] += 1
            if pattern_dict[pattern] == 8:
                print(get_smallest_prime(pattern))
                exit


if __name__ == '__main__':
    main()
