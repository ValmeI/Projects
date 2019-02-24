import calendar
import datetime

'# Create global variable to display the correct month'
month_to_display = datetime.date.today().month
year_to_display = datetime.date.today().year

#print(year_to_display, month_to_display)


tc = calendar.HTMLCalendar(firstweekday=0).formatmonth(year_to_display, month_to_display)
#print(tc)


file = open("calnder_source.html", "w+", encoding='utf-8')
file.write(tc)

