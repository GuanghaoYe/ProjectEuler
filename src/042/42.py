import words


def is_triangle(k):
    t = k * 2
    d = int(t ** 0.5)
    if k == d * (d + 1) / 2:
        return d
    else:
        return 0


def check(s):
    s = s.lower()
    t = 0
    for i in s:
        t += ord(i) - ord('a') + 1
    return is_triangle(t)


def main():
    count = 0
    for i in words.words:
        count += (check(i) != 0)
    print(count)


if __name__ == '__main__':
    main()
