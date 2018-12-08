from datetime import datetime
import sqlite3
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

raw_data_csv = "raw_data.csv"

ZODIAC_SCRAPE = [["Capricornus", "https://www.horoscope.com/zodiac-signs/capricorn", ["Capricorn Greatest Gifts", "Capricorn Greatest Challenges", "Capricorn Secret Weapon"]],
                ["Aquarius", "https://www.horoscope.com/zodiac-signs/aquarius", [" Aquarius Zodiac Sign"]],
                ["Pisces", "https://www.horoscope.com/zodiac-signs/pisces", [" Pisces Zodiac Sign"]],
                ["Aries", "https://www.horoscope.com/zodiac-signs/aries", ["Aries' Greatest Gifts", "Aries' Greatest Challenges", "Aries' Secret Weapon"]],
                ["Taurus", "https://www.horoscope.com/zodiac-signs/taurus", ["Taurus' Greatest Gifts", "Taurus' Greatest Challenges", "Taurus' Secret Weapon"]],
                ["Gemini", "https://www.horoscope.com/zodiac-signs/gemini", ["Gemini's Greatest Gifts", "Gemini's Greatest Challenges", "Gemini's Secret Weapon"]],
                ["Cancer", "https://www.horoscope.com/zodiac-signs/cancer", ["Cancer's Greatest Gifts", "Cancer's Greatest Challenges", "Cancer's Secret Weapon"]],
                ["Leo", "https://www.horoscope.com/zodiac-signs/leo", ["Leo's Greatest Gifts", "Leo's Greatest Challenges", "Leo's Secret Weapon"]],
                ["Virgo", "https://www.horoscope.com/zodiac-signs/virgo", ["Virgo's Greatest Gifts", "Virgo's Greatest Challenges", "Virgo's Secret Weapon"]],
                ["Libra", "https://www.horoscope.com/zodiac-signs/libra", ["Libra's Greatest Gifts", "Libra's Greatest Challenges", "Libra's Secret Weapon"]],
                ["Scorpius", "https://www.horoscope.com/zodiac-signs/scorpio", ["Scorpio's Greatest Gifts", "Scorpio's Greatest Challenges", "Scorpio's Secret Weapon"]],
                ["Sagittarius", "https://www.horoscope.com/zodiac-signs/sagittarius", ["Sagittarius Greatest Gifts", "Sagittarius Greatest Challenges", "Sagittarius Secret Weapon"]]]
                
ZODIAC_LIST = [['Capricornus', 101, 119], ['Aquarius', 120, 218], ['Pisces', 219, 320], ['Aries', 321, 419],
                ['Taurus', 420, 520], ['Gemini', 521, 620], ['Cancer', 621, 722], ['Leo', 723, 822],
                ['Virgo', 823, 922], ['Libra', 923, 1022], ['Scorpius', 1023, 1121], ['Sagittarius', 1122, 1221], ['Capricornus', 1222, 1231]]
conn = sqlite3.connect('zodiac.db') ## Create a sqlite3 connect object
c = conn.cursor() ## Create a cursor object

def scrape_traits(scrape):
    traits_csv = []
    for s in scrape:
        zodiac_sign = []
        zodiac_traits = ""
        html = urlopen(s[1])
        bsObj = BeautifulSoup(html.read(),'html.parser');
        zodiac_sign.append(s[0])
        for traits in bsObj.find_all(["h2", "h3"]):
            if traits.get_text() in s[2]:
                zodiac_traits += traits.get_text()+"/n"
                #print(traits.get_text())
                for elem in traits.next_siblings:
                    found = False
                    if elem.name == 'p':
                        found = True
                        zodiac_traits += elem.get_text()
                        zodiac_sign.append(zodiac_traits)
                        #print(elem.get_text())
                    if found == True:
                        break
        traits_csv.append(zodiac_sign)
    return traits_csv

def write_csv(traits,fn):
    with open(fn, mode='w') as zodiac_file:
        zodiac_writer = csv.writer(zodiac_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for z in traits:
            zodiac_writer.writerow(z)

def create_table():
    """Should check whether the database exists, if not, create it"""
    c.execute('CREATE TABLE IF NOT EXISTS zodiac_traits(keyword TEXT, traits TEXT)')

def data_entry(fn):
    """Enters stuff into the database."""
    with open(fn) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            c.execute("REPLACE INTO zodiac_traits VALUES(?, ?)",(row[0], row[1]))
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
    csv_file = scrape_traits(ZODIAC_SCRAPE)
    write_csv(csv_file,raw_data_csv)
    date = int(zodiac_input()) ## Get and validate user input.
    zodiac = get_zodiac(date) ## Fetch the zodiac sign.
    create_table() ## If zodiac.db does not exist, create it.
    data_entry(raw_data_csv) ## Enters stuff into zodiac.db.
    traits = read_from_db(zodiac)
    print("{}: {}".format(zodiac, traits))