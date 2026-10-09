csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59"""

# | mealtype | mealname                          | mealqty   | price |
# |----------|-----------------------------------|-----------|-------|
# | lunch    | bento box b - sashimi             | box combo | $9.59 |
# | dinner   | vegetable sushi                   | 6 rolls   | $3.50 |
# | dinner   | tuna roll                         | 3 rolls   | $4.50 |
# | dinner   | roe                               | 2 rolls   | $3.95 |
# | lunch    | bento box a - chicken teriyaki    | box combo | $8.59 |
# | dessert  | cheesecake                        | 1 slice   | $8.00 |

def structureCSV(csv_text):
    itemlist = csv_text.split("\n")
    meals = []
    for i, value in enumerate(itemlist):
        templist = value.split(",")
        meals.append({"mealtype":templist[0],"mealname":templist[1],"mealqty":templist[2],"price":templist[3]})
    return meals

# This returns this list:
# meals = [
#   {'mealtype': 'lunch', 'mealname': 'bento box b - sashimi', 'mealqty': 'box combo', 'price': '$9.59'}, 
#   {'mealtype': 'dinner', 'mealname': 'vegetable sushi', 'mealqty': '6 rolls', 'price': '$3.50'}, 
#   {'mealtype': 'dinner', 'mealname': 'tuna roll', 'mealqty': '3 rolls', 'price': '$4.50'}, 
#   {'mealtype': 'dinner', 'mealname': 'roe', 'mealqty': '2 rolls', 'price': '$3.95'}, 
#   {'mealtype': 'lunch', 'mealname': 'bento box a - chicken teriyaki', 'mealqty': 'box combo', 'price': '$8.59'}
# ]

def uniqueMealType(meals):
    unique = []
    for meal in meals:
        if meal["mealtype"] not in unique:
            unique.append(meal["mealtype"])
    return unique
    
print(structureCSV(csv_text))

print(uniqueMealType(structureCSV(csv_text)))

        


