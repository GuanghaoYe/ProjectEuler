import src.algolib.number_theory as nt


def dict_to_set(dic):
    ret = set()
    for key in dic:
        ret.add((key, dic[key]))
    return ret


def main():
    factors = [dict_to_set(nt.factor_naive(2))]
    prefix = [0]
    for i in range(3, 1000000):
        factors.append(dict_to_set(nt.factor_naive(i)))
        if len(factors[-1]) != 4 or len(factors[-1].intersection(factors[-2])) != 0:
            prefix.append(0)
        else:
            prefix.append(prefix[-1] + 1)
            if prefix[-1] == 4:
                print(i - 3)
                return


if __name__ == '__main__':
    main()
