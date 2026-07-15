# Tuple and List Operations in Python

## Problem Statement

Implement the following functions to perform various operations on tuples and lists:

1. **swap_halves** – Swap the first and second halves of an even-length tuple.
2. **swap_at_index** – Split a tuple at index `k` (inclusive) and swap the two parts.
3. **rotate_k** – Rotate a list `k` positions to the right.
4. **first_and_last_index** – Return the first and last occurrence of a given element.
5. **reverse_first_and_last_halves** – Reverse the first and second halves of an even-length list in place.

---

## Python Code

```python
# Swap the first and second halves of an even-length tuple
def swap_halves(items):
    mid = len(items) // 2
    return items[mid:] + items[:mid]


# Split the tuple at index k and swap the two parts
def swap_at_index(items, k):
    return items[k + 1:] + items[:k + 1]


# Rotate the list k positions to the right
def rotate_k(items, k=1):
    k = k % len(items)
    return items[-k:] + items[:-k]


# Find the first and last occurrence of an element
def first_and_last_index(items, elem):
    first = items.index(elem)
    last = len(items) - 1 - items[::-1].index(elem)
    return (first, last)


# Reverse the first and second halves of the list in place
def reverse_first_and_last_halves(items):
    mid = len(items) // 2
    items[:mid] = items[:mid][::-1]
    items[mid:] = items[mid:][::-1]
```

---

## Example 1

### Input

```python
swap_halves((1, 2, 3, 4, 5, 6))
```

### Output

```python
(4, 5, 6, 1, 2, 3)
```

---

## Example 2

### Input

```python
swap_at_index((1, 2, 3, 4, 5), 2)
```

### Output

```python
(4, 5, 1, 2, 3)
```

---

## Example 3

### Input

```python
rotate_k([1, 2, 3, 4, 5], 2)
```

### Output

```python
[4, 5, 1, 2, 3]
```

---

## Example 4

### Input

```python
first_and_last_index([1, 2, 3, 2, 4, 2], 2)
```

### Output

```python
(1, 5)
```

---

## Example 5

### Input

```python
lst = [1, 2, 3, 4, 5, 6]
reverse_first_and_last_halves(lst)
print(lst)
```

### Output

```python
[3, 2, 1, 6, 5, 4]
```

---

## Explanation

- **swap_halves()** divides the tuple into two equal halves and swaps them.
- **swap_at_index()** splits the tuple after index `k` and swaps the resulting parts.
- **rotate_k()** performs a circular right rotation of the list.
- **first_and_last_index()** finds the first and last positions of the given element.
- **reverse_first_and_last_halves()** reverses both halves of the list without creating a new list.

---