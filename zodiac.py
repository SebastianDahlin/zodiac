from datetime import datetime

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
    pass

if __name__ == "__main__":
    get_zodiac()
