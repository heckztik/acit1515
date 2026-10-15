import menu_data
from menu_data import csv_text

def main(datainput):
    meals = menu_data.structureCSV(datainput)
    menuDict = menu_data.organizeMeals(meals)
    uniqueMeals = menu_data.uniqueMeals(menuDict)
    for mealtype in uniqueMeals:
        print(f"* {mealtype.capitalize()} Items *")
        for i in range(len(menuDict[mealtype])):
            print(f" {menuDict[mealtype][i]["price"]}  {menuDict[mealtype][i]["mealname"]}, {menuDict[mealtype][i]["mealqty"]}")

main(csv_text)