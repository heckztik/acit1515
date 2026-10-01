import dow

monthDict = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}


def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))
    monthinput = (input("Month: ").capitalize())
    day = int(input("Day: "))
    
    if monthinput.isnumeric():
        month = int(monthinput)
    else:
        month = monthDict[monthinput]

    if monthinput.isnumeric():
        print(f"{monthinput}/{day}/{year} is a {dow.getDayOfTheWeek(year, month, day)}")
    else:
        print(f"{monthinput} {day}, {year} is a {dow.getDayOfTheWeek(year, month, day)}")


while True:
    print("Would you like to find the weekday on a specific day or would you like to print a calendar?")
    choice = input("Weekday [1], Calendar [2], Quit Program [q] (1/2/q): ")
    if choice == "1":
        getDayOfTheWeekForUserDate()
    elif choice == "2":
        dow.makeCalendar()
    elif choice == "q":
        break
    else:
        print("Invalid selection, please try again.")
