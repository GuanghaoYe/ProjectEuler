def is_recurring(k):
    while k % 2 == 0:
        k /= 2
    while k % 5 == 0:
        k /= 5
    return k > 1


# def get_cycle_length(k):
#     if not is_recurring(k):
#         return 0
#     else:
#         ret = 1
#         denominator = 9
#         while denominator % k:
#             denominator = denominator * 10 + 9
#             ret += 1
#         return ret


def get_cycle_length(k):
    if not is_recurring(k):
        return 0
    else:
        mem = dict()
        cnt = 1
        remainder = 1
        while remainder not in mem:
            mem[remainder] = cnt
            remainder = remainder * 10
            remainder %= k
            cnt += 1
        return cnt - mem[remainder]


ans = 0
maxLen = 0
for i in range(1, 1000):
    cur_len = get_cycle_length(i)
    if cur_len > maxLen:
        ans = i
        maxLen = cur_len

print(ans)
