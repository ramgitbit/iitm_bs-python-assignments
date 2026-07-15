# Manhattan Distance of a Bot (Python)

## Problem Statement
A bot starts at the origin `(0, 0)` and can make the following moves:

- `UP`
- `DOWN`
- `LEFT`
- `RIGHT`

Each move has a magnitude of **1 unit**.

The first input is always `START` and the last input is always `STOP`.

Print the **Manhattan distance** of the bot from the origin.

The Manhattan distance is:

\[
D = |x| + |y|
\]

where `(x, y)` is the final position of the bot.

---

## Python Code

```python
# Initial position of the bot
x = 0
y = 0

# Read moves until STOP is encountered
while True:
    move = input()

    # Ignore the START command
    if move == "START":
        continue

    # Stop taking input
    elif move == "STOP":
        break

    # Update the bot's position
    elif move == "UP":
        y += 1
    elif move == "DOWN":
        y -= 1
    elif move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1

# Print the Manhattan distance
print(abs(x) + abs(y))
```

---

## Example

### Input
```
START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP
```

### Output
```
2
```

### Explanation

Final Position = `(-1, 1)`

Manhattan Distance = `|-1| + |1| = 2`

---
