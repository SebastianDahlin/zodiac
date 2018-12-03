from datetime import datetime

def zodiac_input():
    """Should prompt for user input(no year, just mmdd), validate it and return the value if correct"""
    zodiac_dob = input('Please input your date of birth (mmdd): ')
    try:
        if zodiac_dob != datetime.strptime(zodiac_dob, "%m%d").strftime('%m%d'):
            raise ValueError
        return zodiac_dob
    except ValueError:
        print("Incorrect date format, should be MMDD")
        zodiac_input()
    pass

def get_zodiac():
    """Should return a zodiac based on a date."""
    date = zodiac_input()
    pass

if __name__ == "__main__":
    get_zodiac()
