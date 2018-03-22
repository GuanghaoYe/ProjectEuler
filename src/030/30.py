def digit_5th_powers(k):
    s = str(k)
    ret = 0
    for i in s:
        ret += (ord(i) - ord('0')) ** 5
    return ret


def main():
    ans = 0
    for i in range(2, 1000000):
        if i == digit_5th_powers(i):
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
