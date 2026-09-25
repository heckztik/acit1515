import dow

daysList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayslyList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthDict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def printDayOfTheWeek(year, month, day):
    print(f"{month}-{day}-{year} is a {dow.getDayOfTheWeek(year, month, day)}.")

def printCalendar():
    year = input("Which year would you like to print? : ")
    if dow.isLeapYear(year):
        for month in range(12):
            for day in range(dayslyList[month]):
                printDayOfTheWeek(year, month + 1, day + 1)
    else:
        for month in range(12):
            for day in range(daysList[month]):
                printDayOfTheWeek(year, month + 1, day + 1)



while True:
    print("Would you like to find the weekday on a specific day or would you like to print a calendar?")
    choice = input("Weekday [1], Calendar [2], Quit Program [q] (1/2/q): ")
    if choice == "1":
        dow.runDayOfTheWeek()
    elif choice == "2":
        printCalendar()
    elif choice == "q":
        break
    else:
        print("Invalid selection, please try again.")