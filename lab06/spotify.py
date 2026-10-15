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

def smartTitle(inputstring):
    templist = inputstring.strip().split(" ")
    for word in templist:
        if word.lower() in lowercase_title_words:
            templist[i].replace()

def add_song_input():
    songinput = input("Enter song title: ")
    songinput = songinput.capitalize()
    if lowercase_title_words.capitalize() in songinput:
        magic = #somehow return the word that is there
        songinput.replace(f"{lowercase_title_words[magic]}"
    artistinput = input("Enter srtist: ").title()
    minuteinput = int(input("Enter duration (minutes): "))
    secondinput = int(input("Enter duration (minutes): "))
    duearion = (minuteinput * 60) + secondinput
    return songinput, artistinput, duration

def add_song():
    inputs = add_song_input()
    song = inputs[0]
    if song not in songs:
        pass
    pass

# songs.append({"title": songinput, "artist": artistinput, "duration": duration, "plays": 0}


def record_listen():
    pass

def generate_wrapped():
    pass
    