def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def equal_frac(numerator1, denominator1, numerator2, denominator2):
    if denominator1 == 0 or denominator2 == 0:
        return False
    if numerator1 == 0 or numerator2 == 0:
        return numerator2 == numerator1
    gcd1 = gcd(numerator1, denominator1)
    gcd2 = gcd(numerator2, denominator2)
    numerator1 //= gcd1
    denominator1 //= gcd1
    numerator2 //= gcd2
    denominator2 //= gcd2
    return numerator1 == numerator2 and denominator2 == denominator1


def check(numerator, denominator):
    snumerator = str(numerator)
    sdenominator = str(denominator)
    for i in "123456789":
        if i in snumerator and i in sdenominator:
            snumerator = snumerator.replace(i, '')
            sdenominator = sdenominator.replace(i, '')
    if snumerator == '':
        snumerator = "0"
    if sdenominator == '':
        sdenominator = "0"
    new_numerator = int(snumerator)
    new_denominator = int(sdenominator)
    return new_numerator != numerator and equal_frac(numerator, denominator, new_numerator, new_denominator)


def main():
    ans_numerator = 1
    ans_denominator = 1
    for i in range(10, 100):
        for j in range(10, 100):
            if i < j and check(i, j):
                ans_numerator *= i
                ans_denominator *= j

    gcd_ans = gcd(ans_numerator, ans_denominator)
    ans_numerator //= gcd_ans
    ans_denominator //= gcd_ans
    print(ans_denominator)


if __name__ == '__main__':
    main()
