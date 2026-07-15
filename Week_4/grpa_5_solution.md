# Number Arrow Pattern (Python)

## Problem Statement

Accept a positive integer `n` as input and print a **number arrow** of size `n`.

For example, if `n = 5`, the output should be:

```
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
```

You can assume that `n ≥ 2` for all test cases.

---

## Python Code

```python
# Read the size of the arrow
n = int(input())

# Print the upper half of the arrow
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print the last number without a comma
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()

# Print the lower half of the arrow
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        # Print the last number without a comma
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()
```

---

## Example

### Input

```
5
```

### Output

```
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
```

---

## Explanation

- The first loop prints the pattern from `1` to `n`.
- The second loop prints the pattern from `n-1` back to `1`.
- Commas are printed **between numbers only**, not after the last number of each line.

