import datetime as dt
def calculate_multi_authors(array):
    return ', '.join(array)

def get_datetime_from_weeknum(year, week):
    return dt.datetime.fromisocalendar(year, week, 7) # 7 = SUNDAY