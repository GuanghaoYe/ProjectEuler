def factorial(k):
    ret = 1
    for i in range(1, k + 1):
        ret *= i
    return ret


def check(k):
    s = str(k)
    sum = 0
    for i in s:
        sum += factorial(ord(i) - ord('0'))
    return sum==k


def main():
    ans = 0
    for i in range(10, 2540161):
        if check(i):
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
