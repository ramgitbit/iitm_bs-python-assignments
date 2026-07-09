```python
# Read the size of the arrow
n = int(input())

# Print the upper half (1 to n)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()

# Print the lower half (n-1 to 1)
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()
```