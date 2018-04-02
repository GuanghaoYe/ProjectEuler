from src.algolib.polygon_function import *


def main():
    hexagon = lambda x: x * (2 * x - 1)
    cur = 143
    while 1:
        cur += 1
        t = hexagon(cur)
        if is_pentagonal(t) and is_triangle(t):
            print(t)
            break


if __name__ == '__main__':
    main()
