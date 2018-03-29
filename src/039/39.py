def main():
    p_dict = dict()
    ans = 0
    ans_p = 0
    for i in range(1, 1000):
        for j in range(1, int((1000 ** 2 - i * i) ** 0.5)):
            k = int((i ** 2 + j ** 2) ** 0.5)
            if i ** 2 + j ** 2 == k ** 2:
                p = i + j + k
                if p > 1000:
                    continue
                if p not in p_dict:
                    p_dict[p] = 0
                p_dict[p] += 1
                if p_dict[p] > ans:
                    ans_p = p
                    ans = p_dict[p]
    print(ans_p)


if __name__ == '__main__':
    main()
