def get_alpha_value(x):
    x = x.lower()
    ret = 0
    for c in x:
        ret += ord(c) - ord('a') + 1
    return ret


nameFile = open("./p022_names.txt", "r")
names = nameFile.read()
nameList = [x.strip()[1:-1] for x in names.split(',')]
nameList.sort()
ans = 0
for i in range(0, len(nameList)):
    ans += (i + 1) * get_alpha_value(nameList[i])

print(ans)
