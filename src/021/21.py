def get_d(k):
    ret = 0
    i = 1
    while i * i <= k:
        if k % i == 0:
            ret += i
            ret += k / i
        i = i + 1
    return ret - k


def is_amicable(k):
    a = get_d(k)
    b = get_d(a)
    return b == k and a != k


ans = 0
for i in range(1, 10000):
    if is_amicable(i):
        ans += i

print(ans)
