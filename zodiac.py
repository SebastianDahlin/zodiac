from datetime import datetime
import pprint

ZODIAC_LIST = [['Sagittarius', 1, 19], ['Capricornus', 20, 47], ['Aquarius', 48, 71], ['Pisces', 72, 109], ['Aries', 110, 134], ['Taurus', 135, 171], ['Gemini', 172, 202], ['Cancer', 203, 222], ['Leo', 223, 259], ['Virgo', 260, 304], ['Libra', 305, 327], ['Scorpius', 328, 334], ['Ophiuchus', 335, 352], ['Sagittarius', 353, 365]]

def zodiac_input():
    """Should prompt for user input(no year, just mmdd), validate it and return the value if correct"""
    zodiac_dob = ""
    date_input = input('Please input your date of birth (mmdd): ')

    try:
        if date_input != datetime.strptime(date_input, "%m%d").strftime('%m%d'):
            raise ValueError
        zodiac_dob = date_input
        return zodiac_dob
    except ValueError:
        print("Incorrect date format, should be MMDD")
        return zodiac_input()
    pass

def get_zodiac():
    """Should return a zodiac based on a date."""
    date = zodiac_input()
    mm, dd, day_count, day_to_lookup = int(date[0:2]), int(date[2:4]), 0, 0
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index, month in enumerate(month_list):
        for day in range(1, month + 1):
            day_count += 1
            if mm == index + 1 and dd == day:
                day_to_lookup = day_count
    return [item for item in ZODIAC_LIST if item[1] <= day_to_lookup and item[2] >= day_to_lookup][0][0]

if __name__ == "__main__":
    print(get_zodiac())
