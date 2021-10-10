import datetime

# naive dates and times, can't determine time zones and DST
# aware dates and times, CAN determine TZ and DST

d = datetime.date(2016, 7, 24)

today = datetime.date.today()

# print (today.weekday())
# print (today.isoweekday())
# print(today.day)
# print(d)

# time deltas are differences between dates and times (like durations)
tdelta = datetime.timedelta(days=3)