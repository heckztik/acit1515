songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]

lowercase_title_words = ["a", "an", "the", "and", "but", "or", "nor", "for", "yet", "so", "at", "by", "in", "of", "on", "to", "up", "as", "via"]

def levenshtein(query, target): 
    rows = len(query) + 1
    cols = len(target) + 1
    distance = [[0] * cols for i in range(rows)]    # build table

    for row in range(rows):                         # initialize table
        distance[row][0] = row
    for col in range(cols):
        distance[0][col] = col

    for row in range(1, rows):
        for col in range(1, cols):
            if query[row - 1] == target[col - 1]:   # if it matches
                cost = 0
            else:                                   # if it dont
                cost = 1

            distance[row][col] = min(               # calculate distance
                distance[row - 1][col] + 1, 
                distance[row][col - 1] + 1,
                distance[row - 1][col - 1] + cost
            )

    return distance[rows - 1][cols - 1]
    # thank you claude
    # I think I understand the alg, the filling of the table does the calculation and the bottom right value is the distance. 
    # I have no clue how that translated into this code. 
    # I could spend another 2 hours looking at it to figure it out but I'm tired.

def sortFunc(item):
    return item[1]

def lvsCheck(userinput):
    #normalize input
    norm = userinput.strip().lower()

    #is in library? then return value in lib.
    for song in songs:
        if norm == song["title"]:
            return song["title"]

    #pull from library, len distance 1
    candidates = []
    for song in songs:
        if len(song["title"]) in (len(norm) - 1, len(norm), len(norm) + 1):
            candidates.append((song["title"], song["title"].lower()))
   
    #lev check against list
    matches = []

    for reference, lowered in candidates:
        matches.append((reference, levenshtein(norm, lowered)))

    matches.sort(key=sortFunc)

    #return word that matches closest. if lev distance > 3, return input.
    if matches[0][1] > 3:
        return userinput
    else: 
        return matches[0][0]

def smartTitle(inputstring):
    templist = inputstring.strip().split(" ")
    tempstring = ""

    for song in songs:
        if inputstring not in song["title"]:
            insongs = False
        else:
            insongs = True

    for i, word in enumerate(templist):
        if i == 0:
            templist[i] = word.title()

        elif word.lower() in lowercase_title_words:
            templist[i] = word.lower()

        else:
            templist[i] = word.title()    

    for word in templist:
        tempstring += word + " "

    return tempstring.strip()

def add_song_input():
    songinput = input("Enter song title: ")
    songinputtitle = smartTitle(songinput)
    artistinput = input("Enter artist: ").title()
    minuteinput = int(input("Enter duration (minutes): "))
    secondinput = int(input("Enter duration (seconds): "))
    duration = (minuteinput * 60) + secondinput
    lvs = lvsCheck(songinputtitle)
    
    if lvs != songinput:
        yn = input(f"Did you mean {lvs}? (y/n): ").strip().lower()
        if yn == "y":
            return lvs, artistinput, duration
        else:
            yn = input(f"Did you mean {songinputtitle}? (y/n): ").strip().lower()
            if yn == "y":
                return songinputtitle, artistinput, duration
            else:
                return songinput, artistinput, duration

    print(songinput, songinputtitle, artistinput, duration)


def add_song():
    inputs = add_song_input()
    song = inputs[0]
    artist = inputs[1]
    duration = inputs[2]
    oldliblen = len(songs)
    if not insongs(song):
        print(f"Adding {song}, {artist}, {duration}")
        songs.append({"title": song, "artist": artist, "duration": duration, "plays": 0})
        print(songs[len(songs) - 1])
    else:
        print(f"{song} is already in the library. Did you want to record a listen?")
        if input(f"(y/n): ").lower() == "y":
            record_listen(song)
    if len(songs) == oldliblen:
        print("No new song was added to library.")

# songs.append({"title": songinput, "artist": artistinput, "duration": duration, "plays": 0}

def insongs(query):
    for song in songs:
        if query in songs["title"]:
            return True
        else:
            return False

def record_listen(songtitle):
    if songtitle == None:
        songtitle = input(f"Input title of song: ")
    if not insongs(songtitle):
        print(f"{songtitle} not in library. Please record the song.")
        return False
    for i, song in enumerate(songs):
        if songtitle == song["title"]:
            song["plays"] += 1
            index = i
            recorded = True
    if recorded:
        print(f"{song[index]["title"]} now has {song[index]["plays"]} plays.")
    else:
        print(f"Error: did not record song play. Did not find song in library.")

def generate_wrapped():
    print(f"""
========== YOUR SPOTIFY WRAPPED ==========

Total Songs: {len(songs)}
Total Plays: {# sumof songs["plays"]}
Total Listening Time: 52 minutes

Your Most Played Song:
Numb - Linkin Park (8 plays)

==========================================
""")
    pass
    