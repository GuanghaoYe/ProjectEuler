def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


a = str(factorial(100))
ans = 0
for i in a:
    ans += int(i)-int('0')

print(ans)
