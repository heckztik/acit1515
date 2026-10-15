# Spotify Wrapped

Spotify Wrapped summarizes your listening habits, including your favorite songs, artists, and total listening time. For this lab, I want you to build a simplified Spotify Wrapped Generator. Your program should allow users to add songs, record listens, and generate a summary of their listening habits.

## Part 1 - Store Your Songs

Create a list called `songs` containing dictionaries that represent individual songs.

Below is some (random) song data you can use:

```python
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
```

Notice that each song's duration is represented in seconds.

## Part 2 - Main Menu

Create a program that continuously displays the following menu:

```
====== SPOTIFY WRAPPED ======

1. Add a song
2. Record a listen
3. Generate Spotify Wrapped
4. Exit

Enter your choice:
```

Remember the trick we discussed in lecture about using an infinite `while` loop to keep the program running until the user selects option 4. That might be a good strategy to get this working. 

### Option 1: Add a Song

Ask the user to enter:

- Song title
- Artist name
- Duration (minutes and seconds)

Example:

```python
Enter song title: Blinding Lights
Enter artist: The Weeknd
Enter duration (minutes): 3
Enter duration (seconds): 20
```

Create a dictionary for the new song and append it to the `songs` list.

New songs should have a play count of `0`.

### Option 2: Record a Listen

Ask the user to enter a song title.

Search through the list and increase the matching song's play count by 1.

If the song doesn't exist, display an error message.

### Option 3: Generate Spotify Wrapped

Display the following statistics:

1. **Total songs:** Number of songs in the library.
2. **Total plays:** Sum of all play counts.
3. **Total listening time:** Total minutes spent listening to music, accounting for each song's duration and play count.
4. **Most-played song:** The song with the highest play count.

Example output:

```
========== YOUR SPOTIFY WRAPPED ==========

Total Songs: 3
Total Plays: 16
Total Listening Time: 52 minutes

Your Most Played Song:
Numb - Linkin Park (8 plays)

==========================================
```

<aside>
🚨

Heads up: If the library is empty or no songs have been played, handle those situations appropriately.

</aside>

### Option 4: Exit

Display a goodbye message and terminate the program.

## Part 3 — Functions

I suggest you structure your code as follows:

**`spotify.py`** 

```python
# This file should define and implement the following functions:

# def add_song

# def record_listen

# def generate_wrapped
```

**`main.py`** 

```python
# one example of how you can import the functions
from spotify import add_song, record_listen, generate_wrapped

def main():
	pass

main()
```

<aside>
🤖

When you are done, push your code to your github repository. 

</aside>