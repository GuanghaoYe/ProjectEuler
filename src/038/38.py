def get_pandigital(k):
    ret = ''
    for i in range(1, 10):
        ret += str(i * k)
        if len(ret) >= 9:
            return ret
    return ret


def main():
    nums = list()
    for i in range(1, 10000):
        str = get_pandigital(i)
        if ''.join(sorted(list(str))) == '123456789':
            nums.append(int(str))
    print(max(nums))


if __name__ == '__main__':
    main()
