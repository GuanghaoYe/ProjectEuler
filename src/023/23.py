N = 28123
ans = 0
abundant = dict()


def divisor_sum(k):
    it = k
    ret = 1
    i = 2
    while i * i <= k:
        p = 1
        while k % i == 0:
            p = p * i + 1
            k /= i
        ret *= p
        i += 1
    if k > 1:
        ret *= (k + 1)
    return ret - it


def is_abundant(k):
    if k in abundant:
        return abundant[k]
    else:
        abundant[k] = divisor_sum(k) > k
        return abundant[k]


def check(x):
    i = x // 2
    while i != 0:
        a = i
        b = x - i
        if is_abundant(a) and is_abundant(b):
            return True
        i -= 1
    return False


for i in range(1, N):
    if not check(i):
        ans += i

print(ans)
