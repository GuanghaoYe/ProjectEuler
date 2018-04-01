from src.algolib.polygon_function import *


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
