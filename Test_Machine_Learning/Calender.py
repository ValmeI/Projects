import calendar

tc = calendar.HTMLCalendar(firstweekday=0).formatmonth(2019, 3)
print(tc)


file = open("calnder_source.html", "w+", encoding='utf-8')
file.write(tc)