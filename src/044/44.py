from src.algolib.polygon_function import is_pentagonal


def main():
    f = lambda x: x * (3 * x - 1) // 2
    ans = set()
    for i in range(1, 5000):
        for j in range(i + 1, 5000):
            delta = f(j) - f(i)
            s = f(j) + f(i)
            if is_pentagonal(delta) and is_pentagonal(s):
                ans.add(delta)
    print(min(ans))


if __name__ == '__main__':
    main()
