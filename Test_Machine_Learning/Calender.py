import calendar
import datetime
import locale


'# Create global variable to display the correct month'
month_to_display = datetime.date.today().month
year_to_display = datetime.date.today().year

'# set local to estonia so calender would be in estonian'
locale.setlocale(locale.LC_ALL, 'et_EE')


class MyCustomCalendar(calendar.HTMLCalendar):

    '# so I can change cellspacing and assiene value to it'
    def formatmonth(self, theyear, themonth, cellspacing, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="' + str(cellspacing) + '" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)


def get_month(year, month, cellspacing):
    #html_month = calendar.HTMLCalendar(firstweekday=0).formatmonth()
    html_month = MyCustomCalendar().formatmonth(year, month, cellspacing)
    return html_month


'#Set utf 8 so ä and so on would look ok'
# TODO add bootstrap so it would look acceptable
total = '<meta charset="UTF-8">' + \
        get_month(year_to_display, month_to_display-1, 0) + '<br><br>' + \
        get_month(year_to_display, month_to_display, 0) + '<br><br>' + \
        get_month(year_to_display, month_to_display+1, 0)


'# Write to HTML file to display it'
file = open("calender_source.html", "w+", encoding='utf-8')
file.write(total)

