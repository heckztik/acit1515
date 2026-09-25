
monthcode = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
specialoffsets = {16:6, 17:4, 18:2, 20:6, 21:4}
monthDict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
dotw = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


#  leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400
def isLeapYear(year):
    return int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0)

def getDayOfTheWeek(year, month, day):

    shortenedyear = int(year[len(year) - 2:])
    howmany12s = shortenedyear // 12
    remainder = shortenedyear % 12
    howmany4s = remainder // 4
    century = int(year[:2])

    if century in specialoffsets:
        monthcodewoffset = specialoffsets[century] + monthcode[int(month) - 1]
    else:
        monthcodewoffset = monthcode[int(month) - 1]

    if isLeapYear(year) and (month == 1 or month == 2):
        monthcodewoffset = monthcodewoffset - 1

    dotwIndex = (howmany12s + remainder + howmany4s + int(day) + monthcodewoffset) % 7
    # print(f"shortenedyear: {shortenedyear}, howmany12s: {howmany12s}, remainder: {remainder}, howmany4s: {howmany4s}, day: {day}, monthcodewoffset: {monthcodewoffset}, dotwIndex: {dotwIndex}, dotw: {dotw[dotwIndex]}")
    return dotw[dotwIndex]

# Test isLeapYear() function:
# while True:
#     userinput = input("Is this year a leap year?: ")
#     if userinput == "break":
#         break
#     print(isLeapYear(int(userinput)))

def runDayOfTheWeek():
    print("What day is on this date?")
    year = input("Year: ")

    monthinput = input("Month: ")
    ismonthname = len(monthinput) > 2
    if ismonthname:
        month = monthDict[monthinput]
    else:
        month = int(monthinput)
        # this is terrible
    day = input("Day: ")

    if ismonthname:
        print(f"{monthinput} {day}, {year}")
    else:
        print(f"{monthinput}/{day}/{year}")
    print(f"Is a {getDayOfTheWeek(year, month, day)}.")

# def printCalendar(year):
#     if isLeapYear(year):
#         for day in 365:
#             print(f"{month}-{day}-{year} is a {printDayOfTheWeek()}")

# while True:
#     print("Would you like to find the weekday on a specific day? Or would you like to print a calendar?")
#     choice = input("Weekday [1], Calendar [2], Quit Program [q] (1/2/q): ")
#     if choice == "1":
#         printDayOfTheWeek()
#     # elif choice == "2":
#     #     printCalendar()
#     elif choice == "q":
#         break
#     else:
#         print("Invalid selection, please try again.")
