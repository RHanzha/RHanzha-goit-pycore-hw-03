
from datetime import datetime

today = datetime.today()

date_string = "2021-10-09"
datetime_object = datetime.strptime(date_string, "%Y-%m-%d"
                                    )

get_days_from_today = datetime_object - today
print(get_days_from_today)

#Завдання 2

import random
def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000:
        return []
    if min >= max:
        return []
    if quantity < 1 or quantity > (max - min +1):
        return []


    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1,36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

#Завдання 3
import re

def normalize_phone(phone_number):

    # Очищуємо всі символи крім цифр і плюсів
    clean_number = re.sub(r"[^0-9+]", "", phone_number)

    if clean_number.startswith("00"):
        clean_number = "+" + clean_number[2:] # Якщо номер понається з 00 заміняємо на "+"    
    elif clean_number.startswith("380"):
         clean_number = "+" + clean_number # Якщо номер понається з 380 заміняємо на "+" 
    else:
         clean_number = "+38" + clean_number
    return  clean_number   

#Завдання 4

from datetime import datetime, timedelta
def get_upcoming_birthdays (users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        date_of_birth = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = date_of_birth.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays        
    
users = [
    {"name": "John Doe", "birthday": "1985.11.13"},
    {"name": "Jane Smith", "birthday": "1990.11.17"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)