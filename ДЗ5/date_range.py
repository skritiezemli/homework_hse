from datetime import datetime
from datetime import timedelta


def date_range(start_date, end_date):
    date_list = []
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except:
        return date_list
    while start_date <= end_date:
        date_list.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=1)
    return date_list


print(date_range("2022-01-01", "2022-01-03"))
print(date_range("2022-01-03", "2022-01-01"))
print(date_range("2022-02-30", "2022-02-31"))
