import src.AlgoLibs.numberTheory as nt
import itertools


def get_pandigital_prime(k):
    a = [x for x in range(1, k + 1)]
    ret = 0
    numbers = itertools.permutations(a)
    for num in numbers:
        t = 0
        for d in num:
            t = t * 10 + d
        if nt.is_prime_naive(t):
            ret = max(ret, t)
    return ret


def main():
    ans = 0
    for i in range(1, 10):
        ans = max(ans, get_pandigital_prime(i))
    print(ans)


if __name__ == '__main__':
    main()
