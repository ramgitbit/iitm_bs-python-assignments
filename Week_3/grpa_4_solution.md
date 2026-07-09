# Initial position of the bot
x = 0
y = 0

# Read the first input (START)
move = input()

# Continue taking input until STOP is encountered
while True:
    move = input()

    if move == "STOP":
        break
    elif move == "UP":
        y += 1
    elif move == "DOWN":
        y -= 1
    elif move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1

# Print the Manhattan distance from the origin
print(abs(x) + abs(y))