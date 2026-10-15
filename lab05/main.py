import menu_data
from menu_data import csv_text

csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59
dessert,cheesecake,1 slice,$8.00"""

meals = menu_data.structureCSV(csv_text)
menuDict = menu_data.organizeMeals(meals)
uniqueMeals = menu_data.uniqueMeals(menuDict)

# menuDict = [{
#     'lunch': [
#         {'mealtype': 'lunch', 'mealname': 'bento box b - sashimi', 'mealqty': 'box combo', 'price': '$9.59'}, 
#         {'mealtype': 'lunch', 'mealname': 'bento box a - chicken teriyaki', 'mealqty': 'box combo', 'price': '$8.59'}
#         ], 
#     'dinner': [
#         {'mealtype': 'dinner', 'mealname': 'vegetable sushi', 'mealqty': '6 rolls', 'price': '$3.50'}, 
#         {'mealtype': 'dinner', 'mealname': 'tuna roll', 'mealqty': '3 rolls', 'price': '$4.50'}, 
#         {'mealtype': 'dinner', 'mealname': 'roe', 'mealqty': '2 rolls', 'price': '$3.95'}
#         ]
#     }
# ]

for mealtype in uniqueMeals:
    print(f"* {mealtype.capitalize()} Items *")
    for i in range(len(menuDict[mealtype])):
        print(f" {menuDict[mealtype][i]["price"]}  {menuDict[mealtype][i]["mealname"]}, {menuDict[mealtype][i]["mealqty"]}")
