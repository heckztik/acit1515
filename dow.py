
monthcode = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
specialoffsets = {16:6, 17:4, 18:2, 20:6, 21:4}
monthDict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
dotw = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#  leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def getDayOfTheWeek(year, month, day, lybool):
    year, month, day = int(year), int(month), int(day)

    shortenedyear = year % 100
    howmany12s = shortenedyear // 12
    remainder = shortenedyear % 12
    howmany4s = remainder // 4
    century = year // 100

    if century in specialoffsets:
        monthcodewoffset = specialoffsets[century] + monthcode[month - 1]
    else:
        monthcodewoffset = monthcode[month - 1]

    if lybool:
        monthcodewoffset = monthcodewoffset - 1

    # if isLeapYear(year) and (month == 1 or month == 2):
    #     monthcodewoffset = monthcodewoffset - 1

    dotwIndex = (howmany12s + remainder + howmany4s + int(day) + monthcodewoffset) % 7
    return dotw[dotwIndex]

def runDayOfTheWeek():
    print("What day is on this date?")
    year = int(input("Year: "))
    monthinput = input("Month: ").capitalize()
    day = int(input("Day: "))

    if monthinput.isnumeric():
        month = int(monthinput)
    else:
        month = monthDict[monthinput]    

    if not monthinput.isnumeric():
        print(f"{monthinput} {day}, {year}")
    else:
        print(f"{month}/{day}/{year}")
    print(f"Is a {getDayOfTheWeek(year, month, day, isLeapYear(year))}.")