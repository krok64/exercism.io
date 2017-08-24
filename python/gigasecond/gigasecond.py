from datetime import datetime, timedelta

def add_gigasecond(time):
    delta = timedelta(seconds = 1000000000)
    return time + delta
