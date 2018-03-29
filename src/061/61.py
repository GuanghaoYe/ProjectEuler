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
    f = lambda x: x * (3 * x - 1) / 2
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


# def check(fun, ans, nums):
#     if k >= len(fun):
#         s = set()
#         for i in range(0, k):
#             s.add(fun[i](ans[i]))
#         if len(s) == k and ans[0] // 100 == ans[-1] % 100:
#             return ans
#         else:
#             return False
#
#     for i in range(1, 100):
#         num = (ans[-1] % 100) * 100 + i
#         if num < 1000:
#             continue
#         cur = fun[k](num)
#         if cur:
#             ans.append(num)
#             res = check(fun, k + 1, ans)
#             if res:
#                 return res
#             ans = ans[:-1]
#     return False


def check(funs, ans, nums):
    if len(funs) == 0:
        if ans[0] // 100 == ans[-1] % 100:
            return ans
        else:
            return False
    for i in range(1, 100):
        t = (ans[-1] % 100) * 100 + i
        if t < 1000:
            continue
        for fun in funs:
            cur = fun(t)
            if cur:
                new_ans = ans[:] + [t]
                new_num = ans[:] + [cur]
                remain_funs = funs[:]
                remain_funs.remove(fun)
                res = check(remain_funs, new_ans, new_num)
                if res:
                    return res
    return False


def main():
    funcs = [is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal]
    for i in range(1000, 10000):
        for fun in funcs:
            cur = fun(i)
            if cur:
                remain_funs = funcs[:]
                remain_funs.remove(fun)
                ans = check(remain_funs, [i], [cur])
                if ans:
                    print(ans)
                    print(sum(ans))
                    exit(0)


if __name__ == '__main__':
    main()
