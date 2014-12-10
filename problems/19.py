import datetime
one_day = datetime.timedelta(1)
sundays = 0
date = datetime.date(1901, 1, 1)
while date.year < 2001:
    date = date + one_day
    if date.weekday() == 6 and date.day == 1:
        sundays = sundays + 1

print("Sundays on the first between 1901-01-01 and 2000-12-31: {}".format(sundays))

