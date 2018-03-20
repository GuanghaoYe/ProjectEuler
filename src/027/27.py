def is_prime(k):
    if k < 2:
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i += 1
        return True


def calc_poly(a, b, n):
    return n * n + a * n + b


def get_quadratic_primes(a, b):
    i = 0
    while is_prime(calc_poly(a, b, i)):
        i += 1
    return i


def main():
    len = 0
    a = 0
    b = 0
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            cur = get_quadratic_primes(i, j)
            if cur > len:
                a = i
                b = j
                len = cur
    print(a * b)


if __name__ == "__main__":
    main()
