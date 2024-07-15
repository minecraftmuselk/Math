from calendar import weekday

sundays = 0

for yr in range(1901, 2001):
    for month in range(1, 13):
        if weekday(yr, month, 1) == 6:
            sundays += 1

print(sundays)
