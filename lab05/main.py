import menu_data
from menu_data import csv_text

def main(datainput):
    meals = menu_data.structureCSV(datainput)
    menuDict = menu_data.organizeMeals(meals)
    uniqueMeals = menu_data.uniqueMeals(menuDict)
    for mealtype in uniqueMeals:
        print()
        print(f"* {mealtype.capitalize()} Items *")
        for i in range(len(menuDict[mealtype])):
            print(f" ${(str(float(menuDict[mealtype][i]["price"].replace("$", "")) * 1.8) + "00")[:(str(float(menuDict[mealtype][i]["price"].replace("$", "")) * 1.8) + "00").find(".") + 3]}  {menuDict[mealtype][i]["mealname"]}, {menuDict[mealtype][i]["mealqty"]}")

main(csv_text)