# Tuple & List Operations (IITM BS - Python)

## Question

Complete the following functions.

### 1. swap_halves(items)

Swap the first and second halves of a tuple having an even length.

**Input**

```python
(1,2,3,4)
```

**Output**

```python
(3,4,1,2)
```

---

### 2. swap_at_index(items, k)

Break the tuple at index `k` (the element at index `k` remains in the first part), then swap both parts.

**Input**

```python
(1,2,3,4,5), k = 2
```

**Output**

```python
(4,5,1,2,3)
```

---

### 3. rotate_k(items, k=1)

Return a **new list** after rotating the elements `k` positions to the right.

**Input**

```python
[1,2,3,4,5], k=2
```

**Output**

```python
[4,5,1,2,3]
```

---

### 4. first_and_last_index(items, elem)

Return the first and last occurrence of an element.

**Input**

```python
[1,2,3,2,4,2], 2
```

**Output**

```python
(1,5)
```

---

### 5. reverse_first_and_last_halves(items)

Reverse both halves of an even-length list **in-place**.

**Input**

```python
[1,2,3,4,5,6]
```

**Output**

```python
[3,2,1,6,5,4]
```

---

# Solution

```python
def swap_halves(items):
    """
    Swap the first and second halves of an even-length tuple.
    """
    mid = len(items) // 2
    return items[mid:] + items[:mid]


def swap_at_index(items, k):
    """
    Split the tuple at index k (inclusive),
    then swap both parts.
    """
    return items[k+1:] + items[:k+1]


def rotate_k(items, k=1):
    """
    Rotate the list k positions towards the right.
    Returns a new list.
    """
    k %= len(items)
    return items[-k:] + items[:-k]


def first_and_last_index(items, elem):
    """
    Return the first and last occurrence of elem.
    """
    first = items.index(elem)
    last = len(items) - 1 - items[::-1].index(elem)
    return (first, last)


def reverse_first_and_last_halves(items):
    """
    Reverse the first half and second half of
    the list in-place.
    """
    mid = len(items) // 2

    # Reverse first half
    items[:mid] = items[:mid][::-1]

    # Reverse second half
    items[mid:] = items[mid:][::-1]
```

---

# Concepts Used

## Tuple Slicing

```python
t[:k]
```

Returns elements before index `k`.

```python
t[k:]
```

Returns elements from index `k` onward.

---

## List Rotation

Right rotation by `k`

```python
items[-k:] + items[:-k]
```

Example

```python
[1,2,3,4,5]

↓

[4,5] + [1,2,3]

↓

[4,5,1,2,3]
```

---

## Finding First Occurrence

```python
items.index(elem)
```

Returns the first index.

---

## Finding Last Occurrence

Reverse the list.

```python
items[::-1]
```

Find first occurrence in reversed list.

Convert it back.

```python
len(items)-1-items[::-1].index(elem)
```


---

# Methods Used

### Tuple

- Slicing (`[:]`)
- Concatenation (`+`)

### List

- Slicing
- Reverse (`[::-1]`)
- `index()`
- Slice Assignment

---