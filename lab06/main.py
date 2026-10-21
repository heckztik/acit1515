
import spotify as s

mainmenu = """====== SPOTIFY WRAPPED ======

    1. Add a song
    2. Record a listen
    3. Generate Spotify Wrapped
    4. Exit
    """

def mainLoop():
    print(mainmenu)
    userinput = input("Enter your choice: ").strip().lower()
    if (userinput == "1") or userinput.startswith("add"):
        s.add_song()
    elif (userinput == "2") or userinput.startswith("record"):
        s.record_listen(None)
    elif (userinput == "3") or userinput.startswith(("generate", "wrap")):
        s.generate_wrapped()
    elif userinput == "!print":
        s.printsongs()
    elif (userinput == "4") or userinput.startswith(("quit", "exit")):
        exit(f"Exiting program...")
    elif userinput == "!purge":
        s.purge()
    else:
        print(f"{userinput} is an invalid input. Please try again.")

while True:
    mainLoop()
