import calendar

def find_day(month, day, year):
    return calendar.day_name[
        calendar.weekday(year, month, day)
    ].upper()
