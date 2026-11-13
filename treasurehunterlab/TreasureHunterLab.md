# Treasure Hunter Lab

## Overview

In this lab, you'll build the backend for a simple Treasure Hunt game using Python's built-in `http.server` module, as we’ve been exploring since our previous class.

The game takes place on a 5×5 grid. The player starts in the top-left corner and must find a hidden treasure by moving up, down, left, or right.

You'll be given the HTML, CSS, JavaScript, and a partially completed Python HTTP server. Your job is to implement the missing Python functions that control the game.

### Game Rules

- The grid is 5×5, with coordinates ranging from 0 to 4.
- The player starts at `[0, 0]`.
- The treasure is hidden at `[3, 2]`.
- The player can move up, down, left, or right.
- The player cannot move outside the grid.
- Each valid move increases the move counter by 1.
- The player has a maximum of 10 moves to find the treasure.
- The game ends when the player finds the treasure or runs out of moves.
- Once the game ends, the player cannot move again until the game is restarted.

## Getting Started

I’ve provided some code to help you get started. Copy paste the following code into your code editor:

server.py

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

player = [0, 0]
treasure = [3, 2]
moves = 0

def move_player(direction):
    global player, moves

    pass

def found_treasure():
    pass

def is_game_over():
    pass

def reset_game():
    global player, moves

    pass

def get_game_state():
    return {
        "player": player,
        "found": found_treasure(),
        "moves": moves,
        "game_over": is_game_over(),
    }

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)

        if url.path == "/":
            html = Path("index.html").read_text(encoding="utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif url.path == "/move":
            direction = parse_qs(url.query).get("direction", [""])[0]
            # Note from Armaan: If you're confused about the above line of code...
            # url.query -> "direction=up"
            # parse_qs(url.query) -> {"direction": ["up"]}
            # parse_qs(url.query).get("direction", [""]) -> ["up"]
            # parse_qs(url.query).get("direction", [""])[0] -> "up"

            move_player(direction)

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif url.path == "/reset":
            reset_game()

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

server = HTTPServer(("localhost", 3000), MyHandler)
print("Server running at http://localhost:3000")
server.serve_forever()

```

index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Treasure Hunt</title>

    <style>
        body {
            font-family: Arial, sans-serif;
        }

        #grid {
            display: grid;
            grid-template-columns: repeat(5, 50px);
            gap: 5px;
        }

        .cell {
            width: 50px;
            height: 50px;
            background: lightgray;
            display: grid;
            place-items: center;
            font-size: 24px;
        }

        button {
            padding: 10px 15px;
            margin: 3px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Treasure Hunt</h1>

    <p>Find the hidden treasure in 10 moves or less!</p>

    <div id="grid"></div>

    <p>Moves: <span id="moves">0</span> / 10</p>

    <div>
        <button onclick="move('up')">↑</button>
        <button onclick="move('down')">↓</button>
        <button onclick="move('left')">←</button>
        <button onclick="move('right')">→</button>
    </div>

    <p id="message"></p>

    <button onclick="resetGame()">Restart Game</button>

    <script>
        function draw(player) {
            const grid = document.querySelector("#grid");
            grid.innerHTML = "";

            for (let y = 0; y < 5; y++) {
                for (let x = 0; x < 5; x++) {
                    const cell = document.createElement("div");
                    cell.className = "cell";

                    if (player[0] === x && player[1] === y) {
                        cell.textContent = "🙂";
                    }

                    grid.appendChild(cell);
                }
            }
        }

        function updateGame(data) {
            draw(data.player);

            document.querySelector("#moves").textContent = data.moves;

            const message = document.querySelector("#message");

            if (data.found) {
                message.textContent = "🎉 You found the treasure!";
            } else if (data.game_over) {
                message.textContent = "💀 Game over! You ran out of moves.";
            } else {
                message.textContent = "";
            }
        }

        async function move(direction) {
            const response = await fetch(`/move?direction=${direction}`);
            const data = await response.json();

            updateGame(data);
        }

        async function resetGame() {
            const response = await fetch("/reset");
            const data = await response.json();

            updateGame(data);
        }

        draw([0, 0]);
    </script>
</body>
</html>
```

Open the project in VS Code and run the Python server:

```
python server.py
```

Open your browser and navigate to:

```
http://localhost:3000
```

You should see the Treasure Hunt game. I’ve already implemented a very basic interface for you, but the game won't work correctly until you complete the missing Python functions.

## Understanding the Starter Code

Before writing any code, take a few minutes to understand `server.py`.

You'll notice three global variables:

```
player = [0, 0]
treasure = [3, 2]
moves = 0
```

These variables represent the current state of the game.

- `player` stores the player's current coordinates.
- `treasure` stores the hidden treasure's coordinates.
- `moves` tracks how many valid moves the player has made.

The player's coordinates are stored as `[x, y]`, where `x` represents the horizontal position and `y` represents the vertical position.

For example:

```
player = [2, 3]
```

This means the player is at column 2, row 3.

### How the HTTP Server Works

When a player clicks a direction button, the browser sends an HTTP request to your Python server.

For example, clicking the right arrow sends:

```
GET /move?direction=right
```

Your HTTP server extracts the direction from the URL:

```
direction = parse_qs(url.query).get("direction", [""])[0]
```

It then calls your function:

```
move_player(direction)
```

After processing the move, the server sends the updated game state back to the browser as JSON.

For example:

```json
{
    "player": [1, 0],
    "found": false,
    "moves": 1,
    "game_over": false
}
```

The browser uses this information to update the game interface. Your task is to implement the Python functions that make this possible.

---

## Task 1: Implement `move_player(direction)`

Find the following function in `server.py`:

```python
def move_player(direction):
    global player, moves

    pass
```

This function is responsible for updating the player's position.

### Requirements

1. Check whether the game is already over. If it is, don't allow the player to move.
2. Get the player's current `x` and `y` coordinates.
3. Update the coordinates based on the direction:
    - `"up"` decreases `y` by 1.
    - `"down"` increases `y` by 1.
    - `"left"` decreases `x` by 1.
    - `"right"` increases `x` by 1.
4. Make sure the new coordinates are inside the grid.
5. If the move is valid, update `player` and increase `moves` by 1.
6. If the direction is invalid or the player tries to move outside the grid, don't change the position or move counter.

**Hint:** Below is some pseudocode, but roughly speaking, you could check whether a coordinate is inside the grid using something like:

```
0 <= x < 5
```

You'll need to check both `x` and `y`.

### Testing

Start the game and click the right arrow.

The player should move from:

```
[0, 0]
```

To:

```
[1, 0]
```

The move counter should increase to 1.

Try moving left from `[0, 0]`. The player should remain in the same position, and the move counter should not increase.

---

## Task 2: Implement `found_treasure()`

Find the following function:

```
def found_treasure():
    pass
```

This function checks whether the player has found the treasure.

### Requirements

Return `True` if the player's coordinates are the same as the treasure's coordinates.

Otherwise, return `False`.

For example:

```
player = [3, 2]
treasure = [3, 2]
```

The function should return:

```
True
```

However, if:

```
player = [1, 2]
treasure = [3, 2]
```

The function should return:

```
False
```

**Hint from Armaan:** Python allows you to compare two lists directly using `==`.

### Testing

Move the player to `[3, 2]`.

The browser should display:

```
🎉 You found the treasure!
```

The player should no longer be able to move.

---

## Task 3: Implement `is_game_over()`

Find the following function:

```
def is_game_over():
    pass
```

This function determines whether the game has ended.

### Requirements

The game is over when either of the following conditions is true:

- The player has found the treasure.
- The player has made 10 moves.

Return `True` if either condition is satisfied.

Otherwise, return `False`.

**Hint from Armaan:** You might want to call `found_treasure()` inside this function. You can also use Python's `or` operator to combine conditions, which we’ve already learned from previous lectures.

### Testing

Test both ways of ending the game.

**Test A: Winning**

Move the player onto the treasure at `[3, 2]`.

The game should end immediately, even if the player has moves remaining.

**Test B: Losing**

Make 10 valid moves without finding the treasure.

The browser should display:

```
Game over! You ran out of moves.
```

Try clicking another direction button. The player should not move.

---

## Task 4: Implement `reset_game()`

Find the following function:

```
def reset_game():
    global player, moves

    pass
```

This function resets the game when the player clicks the Restart Game button.

### Requirements

1. Reset the player's position to `[0, 0]`.
2. Reset the move counter to `0`.

The treasure should remain at `[3, 2]`.

### Testing

Make several moves, then click Restart Game.

Verify that:

- The player returns to the top-left corner.
- The move counter displays 0.
- Any previous winning or losing message disappears.
- The player can move again.

---

### Testing Your HTTP Endpoints

You can also test the server directly by entering these URLs into your browser:

**Move right:**

```
http://localhost:3000/move?direction=right
```

**Move down:**

```
http://localhost:3000/move?direction=down
```

**Reset the game:**

```
http://localhost:3000/reset
```

Notice that these endpoints return JSON instead of HTML. Try opening your browser's Developer Tools, selecting the Network tab, and clicking a direction button in the game. Find the HTTP request and inspect its response.

---

## Bonus:

If you finish early, try adding some randomness to the treasure position. Instead of always placing the treasure at `[3, 2]`, generate a random position whenever the game restarts. You can use Python's `random` module. Just make sure the treasure doesn't spawn at the player's starting position.

---

# Debugging Helper Functions

The following functions can help you debug your implementation.

You can copy them into `server.py`, outside the `MyHandler` class.

These functions are optional and are intended to help you inspect and test your game.

## 1. Print the Game State

This function prints the current values of the game's variables.

```python
def print_game_state():
    print("Player:", player)
    print("Treasure:", treasure)
    print("Moves:", moves)
    print("Found:", found_treasure())
    print("Game Over:", is_game_over())
```

Example output:

```
Player: [2, 1]
Treasure: [3, 2]
Moves: 4
Found: False
Game Over: False
```

You can call this function after moving the player to see how the game state changes.

## 2. Print the Game Grid

This function displays the entire grid in your terminal.

```python
def print_grid():
    for y in range(5):
        for x in range(5):
            if player == [x, y]:
                print("P", end=" ")
            elif treasure == [x, y]:
                print("T", end=" ")
            else:
                print(".", end=" ")
        print()
```

Example output:

```
. . . . .
. . P . .
. . . T .
. . . . .
. . . . .
```

Where:

- `P` represents the player.
- `T` represents the treasure.
- `.` represents an empty cell.

If the player and treasure occupy the same position, the grid displays `P`.

## 3. Teleport the Player

This function allows you to manually change the player's position.

It's useful when you want to test whether the treasure detection works without manually moving around the grid.

```python
def teleport_player(x, y):
    global player

    if 0 <= x < 5 and 0 <= y < 5:
        player = [x, y]
```

Example:

```python
teleport_player(3, 2)

print(found_treasure())
# True
```

## 4. Change the Move Counter

This function allows you to manually set the number of moves.

It's useful for testing the game-over condition.

```python
def set_moves(count):
    global moves

    moves = count
```

Example:

```python
set_moves(10)

print(is_game_over())
# True
```

When you are finished, paste your complete solution (html and python) into the boxes below and submit this notion page to the learning up assignment drop box. 

server.py

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import random

player = [0, 0]
treasure = [random.randint(0, 4), random.randint(0, 4)]
moves = 0


def move_player(direction):
    global player, moves
    oldpos = player.copy()

    if found_treasure():
        reset_game()
        player = oldpos.copy()

    if direction == "up" and player[1] > 0:
        player[1] += -1
    elif direction == "down" and player[1] < 4:
        player[1] += 1
    elif direction == "right" and player[0] < 4:
        player[0] += 1
    elif direction == "left" and player[0] > 0:
        player[0] += -1

    if oldpos != player:
        moves += 1


def found_treasure():
    
    if player == treasure:
        return True
    else:
        return False


def is_game_over():
    global moves

    if found_treasure():
        return True

    if moves == 10 and not found_treasure():
        moves = 0
        return True
    else:
        return False


def reset_game():
    global player, moves, treasure
    for i in range(5):
        player = [random.randint(0, 4), random.randint(0, 4)]
        treasure = [random.randint(0, 4), random.randint(0, 4)]
        if not found_treasure():
            break
    moves = 0


def get_game_state():
    return {
        "player": player,
        "found": found_treasure(),
        "moves": moves,
        "game_over": is_game_over(),
    }


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)

        if url.path == "/":
            html = Path("index.html").read_text(encoding="utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif url.path == "/move":
            direction = parse_qs(url.query).get("direction", [""])[0]
            # Note from Armaan: If you're confused about the above line of code...
            # url.query -> "direction=up"
            # parse_qs(url.query) -> {"direction": ["up"]}
            # parse_qs(url.query).get("direction", [""]) -> ["up"]
            # parse_qs(url.query).get("direction", [""])[0] -> "up"

            move_player(direction)

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif url.path == "/reset":
            reset_game()

            data = get_game_state()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())


server = HTTPServer(("localhost", 3000), MyHandler)
print("Server running at http://localhost:3000")
server.serve_forever()

```

index.html (probably nothing has changed, but paste anyways)

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Treasure Hunt</title>

    <style>
        body {
            font-family: Arial, sans-serif;
        }

        #grid {
            display: grid;
            grid-template-columns: repeat(5, 50px);
            gap: 5px;
        }

        .cell {
            width: 50px;
            height: 50px;
            background: lightgray;
            display: grid;
            place-items: center;
            font-size: 24px;
        }

        button {
            padding: 10px 15px;
            margin: 3px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <h1>Treasure Hunt</h1>

    <p>Find the hidden treasure in 10 moves or less!</p>

    <div id="grid"></div>

    <p>Moves: <span id="moves">0</span> / 10</p>

    <div>
        <button onclick="move('up')">↑</button>
        <button onclick="move('down')">↓</button>
        <button onclick="move('left')">←</button>
        <button onclick="move('right')">→</button>
    </div>

    <p id="message"></p>

    <button onclick="resetGame()">Restart Game</button>

    <script>
        function draw(player) {
            const grid = document.querySelector("#grid");
            grid.innerHTML = "";

            for (let y = 0; y < 5; y++) {
                for (let x = 0; x < 5; x++) {
                    const cell = document.createElement("div");
                    cell.className = "cell";

                    if (player[0] === x && player[1] === y) {
                        cell.textContent = "🙂";
                    }

                    grid.appendChild(cell);
                }
            }
        }

        function updateGame(data) {
            draw(data.player);

            document.querySelector("#moves").textContent = data.moves;

            const message = document.querySelector("#message");

            if (data.found) {
                message.textContent = "🎉 You found the treasure!";
            } else if (data.game_over) {
                message.textContent = "💀 Game over! You ran out of moves.";
            } else {
                message.textContent = "";
            }
        }

        async function move(direction) {
            const response = await fetch(`/move?direction=${direction}`);
            const data = await response.json();

            updateGame(data);
        }

        async function resetGame() {
            const response = await fetch("/reset");
            const data = await response.json();

            updateGame(data);
        }

        draw([0, 0]);
    </script>
</body>
</html>
```