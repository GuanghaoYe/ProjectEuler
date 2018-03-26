def get_bin(k):
    return str(bin(k))[2:]


def check(k):
    decimal = str(k)
    binary = get_bin(k)
    return decimal == decimal[::-1] and binary == binary[::-1]


def main():
    ans = 0
    for i in range(1, 1000000):
        if check(i):
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
