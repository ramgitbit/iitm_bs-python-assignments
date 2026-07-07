```python
# ============================================================
# IIT Madras - Python Practice (While Loop)
# ============================================================

# -------------------------------
# Accumulation - Accumulating a final result
# -------------------------------

# 1. sum_until_0
# Continuously read integers from standard input until you receive 0.
# Print the sum of all the integers entered (excluding 0).
total = 0

while True:
    n = int(input())
    if n == 0:
        break
    total += n

print(total) 

# 2. total_price
# Continuously read pairs of integers representing:
#     quantity price
# until the string "END" is received.
# Print the total price of all the items.
total = 0

while True:
    x = input()
    if x == "END":
        break
    qty, price = map(int, x.split())
    total += qty * price

print(total)

# -------------------------------
# Filtering - Selecting based on a criterion
# -------------------------------

# 3. only_ed_or_ing
# Continuously read strings until the word "STOP"
# (case-insensitive, not included in output).
# Print only those strings that end with
# "ed" or "ing" (case-insensitive).

while True:
    s = input()
    if s.lower() == "stop":
        break

    if s.lower().endswith("ed") or s.lower().endswith("ing"):
        print(s)

# 4. reverse_sum_palindrome
# Continuously read positive integers until -1
# (not included in output).
# For each number:
#     reverse the number
#     add the original and reversed numbers
# Print the original number only if the sum is a palindrome.
while True:
    n = int(input())
    if n == -1:
        break

    rev = int(str(n)[::-1])
    total = n + rev

    if str(total) == str(total)[::-1]:
        print(n)


# -------------------------------
# Mapping - Applying the same operation
# -------------------------------

# 5. double_string
# Continuously read lines until an empty line is encountered.
# Print each line repeated twice.
while True:
    s = input()
    if s == "":
        break
    print(s * 2)

# 6. odd_char
# Continuously read strings until a string ending with '.'
# is encountered (include that line in processing).
# Extract characters at odd positions
# (position starts from 1).
# Print the processed strings in a single line
# separated by spaces.
ans = []

while True:
    s = input()

    temp = s[::2]
    ans.append(temp)

    if s.endswith("."):
        break

print(*ans)


# -------------------------------
# Filter and Map
# -------------------------------

# 7. only_even_squares
# Continuously read numbers until "NAN" is encountered.
# Print the square of a number only if it is even.
while True:
    s = input()

    if s == "NAN":
        break

    n = int(s)

    if n % 2 == 0:
        print(n * n)


# -------------------------------
# Filter and Accumulate
# -------------------------------

# 8. only_odd_lines
# Continuously read lines until "END" is encountered
# (END is not included).
# Consider only odd-numbered input lines
# (line numbering starts from 1).
# Build the result by prepending each odd line,
# separated by newline characters.
# Finally print the resulting string,
# which will contain the odd lines in reverse order.
result = ""
line = 1

while True:
    s = input()

    if s == "END":
        break

    if line % 2 == 1:
        if result == "":
            result = s
        else:
            result = s + "\n" + result

    line += 1

print(result)

# ============================================================
```
