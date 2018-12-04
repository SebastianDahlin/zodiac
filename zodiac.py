from datetime import datetime

ZODIAC_LIST = [['Capricornus', 101, 119], ['Aquarius', 120, 218], ['Pisces', 219, 320], ['Aries', 321, 419],
                ['Taurus', 420, 520], ['Gemini', 521, 620], ['Cancer', 621, 722], ['Leo', 723, 822],
                ['Virgo', 823, 922], ['Libra', 923, 1022], ['Scorpius', 1023, 1121], ['Sagittarius', 1122, 1221], ['Capricornus', 1222, 1231]]

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
    z = [z for z in ZODIAC_LIST if date in range(z[1], z[2]+1)]
    return z[0][0]
    
if __name__ == "__main__":
    date = int(zodiac_input())
    print(get_zodiac(date))
