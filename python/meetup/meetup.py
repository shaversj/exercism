from calendar import Calendar
from datetime import date

WEEKDAY_TO_NUMBER = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

DESCRIPTOR = {"1st": 0, "2nd": 7, "3rd": 14, "4th": 21, "5th": 28, "teenth": 12}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_of_the_week, which):
    cal = Calendar()
    daynum = WEEKDAY_TO_NUMBER[day_of_the_week]
    last_days = []

    for weekday in cal.monthdayscalendar(year, month):
        if which in DESCRIPTOR.keys() and weekday[daynum] > DESCRIPTOR[which]:
            return date(year, month, weekday[daynum])
            # meetup_date = date(year, month, weekday[daynum])

        if which == "last" and weekday[daynum] > 20:
            last_days.append(weekday[daynum])

    return date(year, month, max(last_days))

