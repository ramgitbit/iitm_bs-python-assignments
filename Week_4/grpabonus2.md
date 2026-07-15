# List Comprehension Exercises in Python

## Problem Statement

Implement the following functions using **List Comprehensions** wherever applicable.

### Functions

1. **sum_of_squares**
   - Find the sum of the squares of all numbers in a list.

2. **total_cost**
   - Given a list of `(quantity, price)` tuples, calculate the total cost.

3. **abbreviation**
   - Form an abbreviation by taking the first letter of every word and converting it to uppercase.

4. **palindromes**
   - Return a new list containing only palindrome strings.

5. **all_chars_from_big_words**
   - Return a set of all unique characters (in lowercase) from words whose length is greater than 5.

6. **flatten**
   - Convert a nested list into a single list.

7. **unflatten**
   - Convert a flat list into a matrix with the given number of rows.

8. **make_identity_matrix**
   - Create an identity matrix of size `n`.

9. **make_lower_triangular_matrix**
   - Create a lower triangular matrix.

> **Note:** Use **list comprehensions** instead of normal loops wherever possible.

---

# Python Code

```python
# Return the sum of the squares of all numbers
def sum_of_squares(nums):
    return sum([x ** 2 for x in nums])


# Calculate the total cost using (quantity × price)
def total_cost(items):
    return sum([quantity * price for quantity, price in items])


# Create an abbreviation using the first letter of each word
def abbreviation(sentence):
    return ''.join([word[0].upper() for word in sentence.split()])


# Return only palindrome words
def palindromes(words):
    return [word for word in words if word == word[::-1]]


# Return all unique lowercase characters from words longer than 5 letters
def all_chars_from_big_words(sentence):
    return {
        ch.lower()
        for word in sentence.split()
        if len(word) > 5
        for ch in word
    }


# Flatten a nested list
def flatten(matrix):
    return [item for row in matrix for item in row]


# Convert a flat list into a matrix with the given rows
def unflatten(items, rows):
    cols = len(items) // rows
    return [items[i * cols:(i + 1) * cols] for i in range(rows)]


# Create an identity matrix
def make_identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Create a lower triangular matrix
def make_lower_triangular_matrix(m):
    return [[j + 1 if j <= i else 0 for j in range(m)] for i in range(m)]
```

---

# Example 1

### Input

```python
sum_of_squares([1,2,3,4])
```

### Output

```python
30
```

---

# Example 2

### Input

```python
total_cost([(2,50),(3,20)])
```

### Output

```python
160
```

---

# Example 3

### Input

```python
abbreviation("indian institute of technology")
```

### Output

```python
IIOT
```

---

# Example 4

### Input

```python
palindromes(["madam","python","level","racecar"])
```

### Output

```python
['madam', 'level', 'racecar']
```

---

# Example 5

### Input

```python
flatten([[1,2],[3,4],[5,6]])
```

### Output

```python
[1,2,3,4,5,6]
```

---

# Example 6

### Input

```python
make_identity_matrix(3)
```

### Output

```python
[
 [1,0,0],
 [0,1,0],
 [0,0,1]
]
```

---

# Example 7

### Input

```python
make_lower_triangular_matrix(5)
```

### Output

```python
[
 [1,0,0,0,0],
 [1,2,0,0,0],
 [1,2,3,0,0],
 [1,2,3,4,0],
 [1,2,3,4,5]
]
```

---

# Explanation

- **sum_of_squares()** maps every number to its square and then finds the total.
- **total_cost()** multiplies quantity and price for each item and adds them.
- **abbreviation()** takes the first letter of every word and converts it to uppercase.
- **palindromes()** filters only palindrome strings.
- **all_chars_from_big_words()** collects all unique lowercase characters from words longer than five letters.
- **flatten()** converts a 2D list into a 1D list.
- **unflatten()** divides a flat list into equal-sized rows.
- **make_identity_matrix()** creates a matrix with `1`s on the main diagonal and `0`s elsewhere.
- **make_lower_triangular_matrix()** fills numbers on and below the diagonal while keeping the upper triangle as `0`.
