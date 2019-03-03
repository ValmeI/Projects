import calendar
import datetime
import locale


'# Create global variable to display the correct month'
month_to_display = datetime.date.today().month
year_to_display = datetime.date.today().year

'# set local to estonia so calender would be in estonian'
locale.setlocale(locale.LC_ALL, 'et_EE')


def get_month(year, month):
    html_month = calendar.HTMLCalendar(firstweekday=0).formatmonth(year, month)
    return html_month


'#Set utf 8 so ä and so on would look ok'
# TODO add bootstrap so it would look acceptable
total = '<meta charset="UTF-8">' + \
        get_month(year_to_display, month_to_display-1) + '<br><br>' + \
        get_month(year_to_display, month_to_display) + '<br><br>' + \
        get_month(year_to_display, month_to_display+1)


'# Write to HTML file to display it'
file = open("calender_source.html", "w+", encoding='utf-8')
file.write(total)


