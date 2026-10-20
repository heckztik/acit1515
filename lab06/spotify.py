songs = [
    {
        "title": "blinding lights",
        "artist": "the weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "numb",
        "artist": "linkin park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "shape of you",
        "artist": "ed sheeran",
        "duration": 234,
        "plays": 3
    }
]

lowercase_title_words = ["a", "an", "the", "and", "but", "or", "nor", "for", "yet", "so", "at", "by", "in", "of", "on", "to", "up", "as", "via"]

def lvsCheck(userinput):
    #normalize input
    norm = userinput.strip().lower()
    #is in library? then return value in lib.
    for song in songs:
        if norm == song["title"]:
            return norm
    #pull from library, len distance 1
    for song in songs:
        if len(song["title"]) in (len(norm) - 1, len(norm), len(norm) + 1)
            
    #lev check against list
    #return word that matches closest. if lev distance > 3, return input.
    pass

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
    if songinputtitle != songinput:
        if input(f"Did you mean {songinputtitle}? (y/n): ").lower() == "y":
            return songinputtitle, artistinput, duration
        else:
            return songinput, artistinput, duration
    else:
        return songinputtitle, artistinput, duration
    print(songinput, songinputtitle, artistinput, duration)


def add_song():
    inputs = add_song_input()
    song = inputs[0]
    artist = inputs[1]
    duration = inputs[2]
    oldliblen = len(songs)
    if song not in songs:
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

def insongs(input):
    for i, song in songs:
        if song in songs[i]["title"]:
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
    pass
    