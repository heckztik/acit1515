# Python Practice Lab

For this lab, I want you to show me that you understand the fundamental concepts we’ve been covering in Python thus far. For each question, I want you to paste your solution into the code box below each question. When you are finished, submit your notion link to the learning hub drop box. 

### Pick the Longer Word

Write a function called `longerWord(first, second)` that returns whichever word has more characters.

If both words have the same length, return the first word.

```python
def longerWord(first, second):
	if len(second) > len(first):
		print(second)
	else:
		print(first)

longerWord("cat", "elephant")  # returns "elephant"
longerWord("tiger", "bear")    # returns "tiger"
longerWord("sun", "moon")     # returns "moon"
longerWord("red", "sky")      # returns "red"
```

### Dictionary Practice

In the dictionary below:

1. What are the keys?
2. Show how to access the age value
3. Insert a key called hairColor with a value of black
4. Now change that value of hairColor from black to brown
5. Delete the height key and it's value
6. Check if the dictionary has a key called eyeColor, and if it doesn't, print out: "Missing key"
7. Loop through the object, printing the key and value for each pair.

```jsx
person = { "name": "Sarah", "height": "6 feet", "age": 22 }
```

```jsx
1. "name", "height", "age"
2. person["age"]
3. person["hairColor"] = "black"
4. person.update({"hairColor":"brown"})
	 person["hairColor"] = "brown"
5. del person["height"]
6. if "eyeColor" not in person:
	print("Missing Key")
7. for i in person:
	print(i, person[i])

```

### Count Long Words

Write a function called `countLongWords(words, minimumLength)` that counts how many words have **at least** the given number of characters.

An empty list should return `0`.

```python
def countLongWords(words, minimumLength):
	count = []
	for i in words:
		if len(words) == 0:
			print("0")
		elif len(i) >= minimumLength:
			count.append(i)
	return len(count)

countLongWords(["cat", "tiger", "elephant", "dog"], 5)
# returns 2

countLongWords(["a", "to", "and"], 2)
# returns 2
```

### Remove Repeats

Write a function called `removeRepeats(items)` that returns a new list containing each item only once. Keep the first occurrence of each item and preserve the original order. Solve this using lists without using a set (if you don’t know what set is, that’s fine).

```python
def removeRepeats(items):
	slimList = []
	for i in range(len(items)):
		if items[i] not in slimList:
		    slimList.append(items[i])
	print(slimList)


removeRepeats(["apple", "banana", "apple", "pear", "banana"])
# returns ["apple", "banana", "pear"]

removeRepeats([3, 3, 1, 2, 1])
# returns [3, 1, 2]
```

### Security Questions

1. Create a list called `securityQuestions`. Every element (item) in `securityQuestions` will be a dictionary with two keys: `question` and `expectedAnswer`.
2. Fill the `securityQuestions` list with at least three of these dictionaries. Example: one dictionary could be:

    `{ "question": "What was your first pet's name?", "expectedAnswer": "coco" }`
3. Write code that goes through each of the security questions in your list doing the following:

- Use  `input`  to ask the user each question in the securityQuestions list.
- Check whether the user response matches the expected answer. If the answer does match, go ahead and ask the next question, but if the answer does not match, stop asking the user questions and show a message saying: "Invalid response, please try again later".
- If the user successfully answers all the questions, print: "Success. You may now access your account".

```python
securityQuestions = [
{"question":"What was your first pet's name?", "expectedAnswer":"Coco"},
{"question":"What was the street you grew up on?", "expectedAnswer":"Main Street"},
{"question":"What is your Mother's maiden name?", "expectedAnswer":"Collins"},
]
auth = True
for i in range(len(securityQuestions)):
	if input(securityQuestions[i]["question"] + " ") != securityQuestions[i]["expectedAnswer"]:
		print("Invalid response, please try again later")
		auth = False
		break
if auth == True:
	print("Success. You may now access your account")
```

### Login

1. Create a dictionary called `login` with a key for the user's name and a key for the user's password. The values can be whatever you want.
2. Write code that uses `input` to ask the user for their password with a message that includes their username. Example: If the user name you created is `sarah123`, the message should be `"Enter password for sarah123: "`
3. Check if the password entered by the user matches the password in the `login` dictionary. If it matches, you can print out: "You may access your account" and end the program.
4. If the passwords do not match, make the user retry entering their password. You must keep showing them this message until they enter a correct password.
5. Now that you’ve gotten that working, I want you to modify your code to give the user **only three chances** to enter the correct password. If they fail to enter a correct password after 3 tries, you must exit the program, saying to the user: "You have tried too many times.". The solution you paste below should be the version that gives the user only three chances.

```py
login = {"username":"sarah123", "password":"securepassword"}

for attempts in range(3):
    if input(f"Enter password for {login["username"]}: ") == login["password"]:
        print("You may access your account")
				break
    elif attempts == 2:
        print("You have tried too many times.")
    else:
        print("Incorrect password. Please try again.")
```

### Uppercase Odds

In this problem, convert a normal string into `uppercaseOddWords` text. This function should convert every other word in a sentence to uppercase. 

So given the following sentence:

```
"fur pillows are hard to actually sleep on"
```

Your function should return:

```
"fur PILLOWS are HARD to ACTUALLY sleep ON"
```

(Note: we are starting to count at 0)

```py
def uppercaseOddWords(userinput):
    newstring = ""
    words = userinput.split(" ")
    for i in range(len(words)):
        if i % 2:
            newstring = newstring + words[i].upper() + " "
        else:
            newstring = newstring + words[i] + " "
    return newstring.strip()

print(uppercaseOddWords(input("Input a sentence to convert every other word to uppercase: ")))
```

### upperCamelCase

You will receive a normal string of words separated with spaces as the input. Your job is to convert this string into an upper camel cased strings.

Your Code:

```python
def upperCamelCase(userinput):
    newstring = ""
    words = userinput.split()
    for i in range(len(words)):
        newstring = newstring + words[i][0].upper() + words[i][1:]
    return newstring

def upperCamelCaseMethod(userinput)
  print(userinput.strip().title().replace(" ", ""))

print(upperCamelCase("fur pillows are hard to actually sleep on"))
```

Expected Output

```
FurPillowsAreHardToActuallySleepOn
```

### Count words

Do you ever listen to a song and wonder how many times the artist says each word in the song? Probably not…but let’s make a program that can figure this out anyways! For example, we want our program to be able to figure out how many times Daft Punk say the word `it` in their song `Technologic`.

It’s 399!

Your function will receive an array of words and will have to return an object where the **key** is the word, and the **value** is the number of times that word appears in the array.

For example, if the input was

`"buy it use it break it fix it trash it change it mail upgrade it"`

then the output would be:

```jsx
{
  "buy": 1,
  "it": 7,
  "use": 1,
  "break": 1,
  "fix": 1,
  "trash": 1,
  "change": 1,
  "mail": 1,
  "upgrade": 1
}
```

(Don’t worry if the order of the keys/values look different for you, that doesn’t matter)

Your code:

```python
def countWords(inputs):
    wordcountDict = {}
    words = inputs.split()
    for i in range(len(words)):
        if words[i] not in wordcountDict:
            wordcountDict[words[i]] = 1
        else: 
						wordcountDict[words[i]] = wordcountDict[words[i]] + 1
    return wordcountDict


inputs = "buy it use it break it fix it trash it change it mail upgrade it"
output = countWords(inputs)
print(output)
```

### Word Position

Create a function called **wordPosition** which takes a list of words, and returns the indices where each word shows up in the list. Take a look at the comment below to see how the output should look. Your output should have the same structure as the sample shown in the comment. The order of the keys in the dictionary does not matter. This question is basically the same as the last one, but instead of counting the words, we want to know the index of each word.

```python
inputs = [
  "buy",
  "it",
  "use",
  "it",
  "break",
  "it",
  "fix",
  "it",
  "trash",
  "it",
  "change",
  "it",
  "mail",
  "upgrade",
  "it",
]

def wordPosition(inputs):
    positionDict = {}
    for i in range(len(inputs)):
        if inputs[i] not in positionDict:
            positionDict[inputs[i]] = []
        positionDict[inputs[i]].append(i)
    return positionDict

output = wordPosition(inputs)
print(output)

# Output should look roughly similar to below:
# {
#  "break": [ 4 ],
#  "buy": [ 0 ],
#  "change": [10],
#  "fix": [ 6 ],
#  "it":  [1, 3, 5, 7, 9, 11, 14],
#  "mail": [ 12 ],
#  "trash": [ 8 ],
#  "upgrade": [ 13 ],
#  "use": [ 2 ]
# }

# Note: the [] above are lists
# The ordering of the keys does not matter
```

### Song Organizer

You are given a list of artist dictionaries and need to create a single dictionary to organize them based on their year.

### Input

```python
artists = [
  {
    "song": "HOLIDAY",
    "name": "Lil Nas X",
    "year": 2020,
  },
  {
    "song": "Say So",
    "name": "Doja Cat",
    "year": 2020,
  },
  {
    "song": "Old Town Road",
    "name": "Lil Nas X",
    "year": 2019,
  },
  {
    "song": "Bad Guy",
    "name": "Billie Eilish",
    "year": 2019,
  },
  {
    "song": "God's Plan",
    "name": "Drake",
    "year": 2018,
  },
]

def artistsByYear(artists):
    byyearDict = {}
    for i, song in enumerate(artists):
        if str(song["year"]) not in byyearDict:
            byyearDict[str(song["year"])] = []
            byyearDict[str(song["year"])].append(song)
        else:
            byyearDict[str(song["year"])].append(song)
    return byyearDict

print(artistsByYear(artists))
```

### Expected Output

```jsx
{
  "2018": [
    {
      "song": "God's Plan",
      "name": "Drake",
      "year": 2018
    }
  ],
  "2019": [
    {
      "song": "Old Town Road",
      "name": "Lil Nas X",
      "year": 2019
    },
    {
      "song": "Bad Guy",
      "name": "Billie Eilish",
      "year": 2019
    }
  ],
  "2020": [
    {
      "song": "HOLIDAY",
      "name": "Lil Nas X",
      "year": 2020
    },
    {
      "song": "Say So",
      "name": "Doja Cat",
      "year": 2020
    }
  ]
}
```