def main():
    s = '0'
    cnt = 1
    while len(s) <= 1000000:
        s += str(cnt)
        cnt += 1
    ans = 1
    for i in range(0, 7):
        ans *= int(s[10 ** i])
    print(ans)


if __name__ == '__main__':
    main()
