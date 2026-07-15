# Prime Factors of a Number (Python)

## Problem Statement
Accept a positive integer `n`, where `n > 1`, as input from the user and print all the **prime factors** of `n` in **ascending order**.

## Python Code

```python
# Read the input
n = int(input())

# Start checking from the smallest prime number
i = 2

# Continue until i becomes greater than n
while i <= n:
    # If i is a factor of n
    if n % i == 0:
        # Print the prime factor
        print(i)

        # Remove all occurrences of this prime factor
        while n % i == 0:
            n //= i

    # Check the next number
    i += 1
```

## Example 1

**Input**
```
12
```

**Output**
```
2
3
```

---

## Example 2

**Input**
```
100
```

**Output**
```
2
5
```

---
