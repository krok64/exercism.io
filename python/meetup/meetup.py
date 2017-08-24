from datetime import date, timedelta

month_list = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12 }
num_list = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th': 5}
days_of_week = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7 }

def meetup_day(year, month, week_day, num):
    week_day = days_of_week[week_day]
    this_date = date(2000,1,1)
    delta=0
    def get_delta(day):
        delta = 0
        this_date = date(year=year, month=month, day=day)
        first_month_day = this_date.isoweekday()
        if first_month_day != week_day:
            delta = week_day - first_month_day
            if delta < 0:
                delta = delta + 7
        return (delta, this_date)

    if num in num_list:
        delta, this_date = get_delta(1)
        delta = delta + 7 * (num_list[num] - 1)
        if (this_date + timedelta(days=delta)).month != month:
        	raise Exception()

    if num == 'last':
        delta, this_date = get_delta(28)
        if (this_date + timedelta(days=delta)).month != month:
            delta = delta - 7

    if num=='teenth':
        delta, this_date = get_delta(13)

    return this_date + timedelta(days=delta)
