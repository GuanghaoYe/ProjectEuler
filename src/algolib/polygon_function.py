def is_triangle(k):
    t = k * 2
    d = int(t ** 0.5)
    if k == d * (d + 1) / 2:
        return d
    else:
        return 0


def is_square(k):
    if int(k ** 0.5) ** 2 == k:
        return int(k ** 0.5)
    else:
        return 0


def binary_search(k, f):
    l = 0
    r = 100000
    while r - l > 1:
        mid = (l + r) // 2
        if f(mid) <= k:
            l = mid
        else:
            r = mid
    return l


def is_pentagonal(k):
    f = lambda x: x * (3 * x - 1) // 2
    ret = binary_search(k, f)
    if f(ret) == k:
        return ret
    else:
        return 0


def is_hexagonal(k):
    f = lambda x: x * (2 * x - 1)
    ret = binary_search(k, f)
    if f(ret) == k:
        return ret
    else:
        return 0


def is_heptagonal(k):
    f = lambda x: x * (5 * x - 3) / 2
    ret = binary_search(k, f)
    if f(ret) == k:
        return ret
    else:
        return 0


def is_octagonal(k):
    f = lambda x: x * (3 * x - 2)
    ret = binary_search(k, f)
    if f(ret) == k:
        return ret
    else:
        return 0