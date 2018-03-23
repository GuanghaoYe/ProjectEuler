def check(k):
    i = 1
    while i * i <= k:
        if k % i == 0:
            a = i
            b = k // i
            s = str(a) + str(b) + str(k)
            if ''.join(sorted(s)) == '123456789':
                return True
        i += 1
    return False


def main():
    sum = 0
    for i in range(1, 100000):
        if check(i):
            sum += i
    print(sum)


if __name__ == '__main__':
    main()
