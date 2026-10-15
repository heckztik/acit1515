# Week 5 Lab

Instructions:  

The following lab is due ***by* the start of your next class with me. Please use your given name + preferred name if they are different:**

Your full name : ____________________

Your Student Number: _______________

### Submission Process:

Notion is a tool which allows you to easily paste code and submit it to me. Go to [https://www.notion.so/](https://www.notion.so/) to make an account, and then once logged into notion, create a page which you will use to answer the questions in this challenge. 

You will see an area in the top right corner that says "Duplicate". Click this. 

![](Untitled.png)

You will now have a copy of the Lab instructions within your Notion account. Fill in the answers to the questions.

![](Untitled%201.png)

After you are ready, click the "share" button in the top right corner. Change tabs to the Publish Tab.

![Untitled](Untitled%202.png)

Click the **Publish to web** button**.**

![Untitled](Untitled%203.png)

Next, turn on **Allow editing & Allow comments. Then click Copy web link**:

![Untitled](Untitled%204.png)

Lastly, go to the **Activities > Assignments** section of learning hub, click the assignment, and then paste the notion link you copied into the text box. Click Submit.  

![](Untitled%205.png)

**Failing to follow these instructions will result in no credit being awarded for the lab.**

Your task is to convert a CSV containing items on a restauraunt menu to a TXT file. A CSV file is a **comma seperated values** file, where each line represents one entry, and each part of the entry is seperated by a comma. For now, we won’t worry about reading and writing files and just use in-memory strings and our terminal.

To get started, create a file in VS Code called `menu_data.py` and paste the following contents into your VS Code window:

```python
csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59"""
```

Your program needs to take the content above, format it ***as closely as possible*** to the example below, and print it out. (Note the spacing, indentation, etc, formatting each price to 2 decimals):

```
* Lunch Items *
 $15.46 bento box a - chicken teriyaki, box combo  
 $17.26	bento box b – sashimi, box combo  

* Dinner Items *
 $7.11	roe, 2 rolls   
 $8.10	tuna roll, 3 rolls  
 $6.30	vegetable sushi, 6 rolls
```

The CSV could change to look like the following (note that we added dessert):

```python
csv_text = """lunch,bento box b - sashimi,box combo,$9.59
dinner,vegetable sushi,6 rolls,$3.50
dinner,tuna roll,3 rolls,$4.50
dinner,roe,2 rolls,$3.95
lunch,bento box a - chicken teriyaki,box combo,$8.59
dessert,cheesecake,1 slice,$8.00"""
```

which would require your program to output a text file like so:

```
* Lunch Items *
 $15.46	bento box a - chicken teriyaki, box combo  
 $17.26	bento box b – sashimi, box combo  

* Dinner Items *
 $7.11	roe, 2 rolls   
 $8.10	tuna roll, 3 rolls  
 $6.30	vegetable sushi, 6 rolls

* Dessert Items *
 $14.40	cheesecake, 1 slice   
```

In other words, you cannot assume that the CSV will always contain either Lunch or Dinner. The category could be anything (ex, Dessert, Drinks, Appetizers, etc). Here is what you ***can*** guarantee:

The following structure will always hold true:

```jsx
[Meal Type] [Meal Name] [Meal Quantity] [Price]
```

In the same directory as your `menu_data.py` file, create a file called `main.py` 

```python
from menu_data import csv_text

# call your helper functions from in here

def structureCSV(csv_text):
    itemlist = csv_text.split("\n")
    meals = []
    for value in itemlist:
        templist = value.split(",")
        meals.append({"mealtype":templist[0],"mealname":templist[1],"mealqty":templist[2],"price":templist[3]})
    return meals

def organizeMeals(meals):
    menuDict = {}
    for mealtype in meals:
        if str(mealtype["mealtype"]) not in menuDict:
            menuDict[str(mealtype["mealtype"])] = []
        menuDict[str(mealtype["mealtype"])].append(mealtype)
    return menuDict

def uniqueMeals(menuDict):
    uniqueMeals = []
    for type in menuDict:
        uniqueMeals.append(type)
    return uniqueMeals

def main(datainput):
    meals = structureCSV(datainput)
    menuDict = organizeMeals(meals)
    uniqueMeals = uniqueMeals(menuDict)
    for mealtype in uniqueMeals:
        print()
        print(f"* {mealtype.capitalize()} Items *")
        for i in range(len(menuDict[mealtype])):
            print(f" ${(str(float(menuDict[mealtype][i]["price"].replace("$", "")) * 1.8) + "00")[:(str(float(menuDict[mealtype][i]["price"].replace("$", "")) * 1.8) + "00").find(".") + 3]}  {menuDict[mealtype][i]["mealname"]}, {menuDict[mealtype][i]["mealqty"]}")

main(csv_text)

```

When you run your program, you *should* be able to see the `csv_text` printed out. At this point, you should start creating helper functions and calling them from in your `main` function. 

<aside>
💡

Paste your solution into the code box above and submit your Notion page to the learning hub drop box. 

</aside>