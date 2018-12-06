from datetime import datetime
import sqlite3

ZODIAC_LIST = [['Capricornus', 101, 119], ['Aquarius', 120, 218], ['Pisces', 219, 320], ['Aries', 321, 419],
                ['Taurus', 420, 520], ['Gemini', 521, 620], ['Cancer', 621, 722], ['Leo', 723, 822],
                ['Virgo', 823, 922], ['Libra', 923, 1022], ['Scorpius', 1023, 1121], ['Sagittarius', 1122, 1221], ['Capricornus', 1222, 1231]]
conn = sqlite3.connect('zodiac.db') ## Create a sqlite3 connect object
c = conn.cursor() ## Create a cursor object

def create_table():
    """Should check whether the database exists, if not, create it"""
    c.execute('CREATE TABLE IF NOT EXISTS zodiac_traits(keyword TEXT, traits TEXT)')

def data_entry():
    """Enters stuff into the database"""
    c.execute("REPLACE INTO zodiac_traits VALUES('Capricornus', 'You sir, are an idiot!')")
    c.execute("REPLACE INTO zodiac_traits VALUES('Aquarius', 'You sir, are an idiot!')")
    c.execute("REPLACE INTO zodiac_traits VALUES('Pisces', 'You sir, are an idiot!')")
    c.execute("REPLACE INTO zodiac_traits VALUES('Aries', 'You sir, are an idiot!')")
    conn.commit()

def read_from_db(zodiac):
    """Should return traits for given zodiac"""
    zodiac_data = {}
    c.execute('SELECT * FROM zodiac_traits')
    for row in c.fetchall():
        zodiac_data[row[0]] = row[1]
    c.close()
    conn.close()
    try:
        return(zodiac_data[zodiac])
    except:
        return("No traits available")
    

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
    date = int(zodiac_input()) ## Get and validate user input.
    zodiac = get_zodiac(date) ## Fetch the zodiac sign.
    create_table() ## If zodiac.db does not exist, create it.
    data_entry() ## Enters stuff into zodiac.db.
    traits = read_from_db(zodiac)
    print("{}: {}".format(zodiac, traits))