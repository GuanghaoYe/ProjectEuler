import math


def get_digit(k):
    phi = (math.sqrt(5) + 1) / 2
    return math.ceil(k * math.log10(phi) - math.log10(5) / 2)


l = 1
r = 100000

while r - l > 1:
    mid = (l + r) // 2
    if get_digit(mid) >= 1000:
        r = mid
    else:
        l = mid

print(r)
