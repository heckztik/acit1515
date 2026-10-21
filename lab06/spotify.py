from songdata import songs

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
    validinput = False
    while not validinput:
        minuteinput = input("Enter duration (minutes): ").strip()
        secondinput = input("Enter duration (seconds): ").strip()
        if minuteinput.isdecimal() and secondinput.isdecimal():
            validinput = True
            minuteinput = int(minuteinput)
            secondinput = int(secondinput)
        else:
            print(f'"{minuteinput}" or "{secondinput}" is not a valid input. Please only input intergers.')
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
    return songinput, artistinput, duration

    print(songinput, songinputtitle, artistinput, duration)


def add_song():
    inputs = add_song_input()
    print(inputs)
    song = inputs[0]
    artist = inputs[1]
    duration = inputs[2]
    oldliblen = len(songs)
    if not insongs(song):
        print(f"Adding {song}, {artist}, {duration} at index {len(songs)}")
        songs.append({"title": song, "artist": artist, "duration": duration, "plays": 0})
    else:
        print(f"{song} is already in the library. Did you want to record a listen?")
        if input(f"(y/n): ").lower() == "y":
            record_listen(song)
    if len(songs) == oldliblen:
        print("No new song was added to library.")

# songs.append({"title": songinput, "artist": artistinput, "duration": duration, "plays": 0}

def insongs(query):
    for song in songs:
        if query == song["title"]:
            return True
    return False

def incrementPlayCount(songtitle):
    increment = False
    for song in songs:
        if song["title"] == songtitle:
            song["plays"] += 1
            print(f"{song["title"]}'s playcount is now {song["plays"]}")
            increment = True
    if not increment:
        print(f"Error, {songtitle}'s playcount was not incremented properly.")

def record_listen(songtitle):
    if songtitle == None:
        songtitle = smartTitle(input(f"Input title of song: "))
        lvs = lvsCheck(songtitle)
    if (not insongs(songtitle)) and insongs(lvs):
        if input(f"Did you mean {lvs}? (y/n): ").lower().startswith("y"):
            incrementPlayCount(lvs)
    elif (not insongs(songtitle)) and (not insongs(lvs)):
        print(f"Did not find song in library. Please try again")
        return False
    else:
        incrementPlayCount(songtitle)
        return True

def playcount(list):
    return list["plays"]

def printsongs():
    print(songs)

def purge():
    songs = []

def generate_wrapped():
    if len(songs) == 0:
        print(f"No songs to wrap. Please enter some songs first.")
    else:
        plays = 0
        for song in songs:
            plays += song["plays"]
        listentime = 0
        for song in songs:
            listentime += song["plays"] * song["duration"]
        listentime = listentime // 60
        templist = songs.copy()
        templist.sort(reverse=True, key=playcount)
        mostplayed = templist[0]

        print(f"""
========== YOUR SPOTIFY WRAPPED ==========

Total Songs: {len(songs)}
Total Plays: {plays}
Total Listening Time: {listentime} minutes

Your Most Played Song:
{mostplayed["title"]} - {mostplayed["artist"]} ({mostplayed["plays"]} plays)

==========================================
""")
