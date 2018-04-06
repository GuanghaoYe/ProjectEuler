def main():
    ans = 0
    for i in range(1, 1001):
        ans += i ** i
    print(ans % (10 ** 10))


if __name__ == '__main__':
    main()
