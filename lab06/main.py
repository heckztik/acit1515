from spotify import add_song, record_listen, generate_wrapped


# Temp song data so I don't need to re-record everytime I run the loop.
# !!! MAKE SURE TO INIT LIST IN FINAL AND NOT USE OLD SONG DATA !!!
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

mainmenu = """====== SPOTIFY WRAPPED ======

    1. Add a song
    2. Record a listen
    3. Generate Spotify Wrapped
    4. Exit
    """

def mainLoop():
    print(mainmenu)
    userinput = input("Enter your choice: ")
    if userinput == "1":
        add_song()
    elif userinput == "2":
        record_listen()
    elif userinput == "3":
        generate_wrapped()
    elif userinput == "print":
        print(songs)
    elif userinput == "4":
        exit()
    else:
        print(f"{userinput} is an invalid input. Please try again.")

while True:
    # songs = [] 
    mainLoop()
