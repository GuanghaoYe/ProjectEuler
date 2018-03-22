def main():
    s = set()
    for i in range(2, 101):
        for j in range(2, 101):
            s.add(i ** j)

    print(s.__len__())


def main2():
    s = set()
    ans = 0
    for i in range(2, 101):
        if i in s:
            continue
        p = 1
        s2 = set()
        while i ** p <= 100:
            s.add(i ** p)
            for j in range(2, 101):
                s2.add(p * j)
            p += 1
        ans += s2.__len__()
    print(ans)


if __name__ == '__main__':
    main()
    main2()
