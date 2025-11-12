from datetime import datetime

today = datetime.today()

date_string = "2021-10-09"
datetime_object = datetime.strptime(date_string, "%Y-%m-%d"
                                    )

get_days_from_today = datetime_object - today
print(get_days_from_today)
