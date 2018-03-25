def get_prime_list(n):
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


def main():
    primes = get_prime_list(1000000)
    prime_set = set(primes)
    ans_set = set()
    for i in primes:
        s = str(i)
        new_str = s
        flag = True
        for offset in range(1, len(s)):
            new_str = new_str[-1:] + new_str[:-1]
            if not int(new_str) in prime_set:
                flag = False
        if flag:
            ans_set.add(i)
    print(len(ans_set))


if __name__ == '__main__':
    main()
