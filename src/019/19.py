start = (1900, 1, 1)
end = (2000, 12, 31)

day = 1
cnt = 0
cur = start

monthToDay = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap(year):
    if year % 4:
        return False
    else:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True


def get_days(date):
    return monthToDay[date[1]] + (date[1] == 2) * (is_leap(date[0]))


def next(date):
    next_day = date[2] + 1
    next_month = date[1]
    if next_day > get_days(date):
        next_day -= get_days(date)
        next_month += 1
    next_year = date[0]
    if next_month > 12:
        next_month -= 12
        next_year += 1
    if next_day != date[0]:
        print(next_year)
    return next_year, next_month, next_day


while cur != end:
    cur = next(cur)
    day += 1
    if cur[2] == 1:
        cnt += (day % 7 == 0)
    if cur == (1900, 12, 31):
        cnt = 0

print(cnt)
