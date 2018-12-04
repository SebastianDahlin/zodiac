from datetime import datetime

ZODIAC_LIST = [['Capricornus', '0101', '0119'], ['Aquarius', '0120', '0218'], ['Pisces', '0219', '0320'], ['Aries', '0321', '0419'], ['Taurus', '0420', '0520'], ['Gemini', '0521', '0620'], ['Cancer', '0621', '0722'], ['Leo', '0723', '0822'], ['Virgo', '0823', '0922'], ['Libra', '0923', '1022'], ['Scorpius', '1023', '1121'], ['Sagittarius', '1122', '1221'], ['Capricornus', '1222', '1231']]

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

def get_zodiac(date):
    """Should return a zodiac based on a date."""
    date = datetime.strptime(date, "%m%d")
    for zodiac in ZODIAC_LIST:
        start_date = datetime.strptime(zodiac[1], "%m%d")
        end_date = datetime.strptime(zodiac[2], "%m%d")
        if start_date <= date and end_date >= date:
            return(zodiac[0])

if __name__ == "__main__":
    date = zodiac_input()
    get_zodiac(date)
