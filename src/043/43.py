import itertools
from functools import reduce
import src.AlgoLibs.numberTheory as nt

check_list = nt.prime_linear_sieve(18)


def check(nums):
    # if nums == [1, 4, 0, 6, 3, 5, 7, 2, 8, 9]:
    #     print("wow")
    for i in range(1, 8):
        if reduce((lambda acc, x: acc * 10 + x), nums[i:i + 3]) % check_list[i - 1]:
            return False
    return True


def main():
    a = [x for x in range(0, 10)]
    numbers = itertools.permutations(a)
    ans = 0
    for number in numbers:
        if check(number):
            ans += reduce((lambda acc, x: acc * 10 + x), number)
    print(ans)


if __name__ == '__main__':
    main()
