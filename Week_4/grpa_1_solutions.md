# List Mutating & Non-Mutating Operations | Set Operations (IITM BS - Python)

## Question

Implement the following three functions:

### 1. `list_mutating_operations(items, item1, item2)`

Perform the following operations **in-place** (do not create a new list):

1. Sort the list.
2. Append `item1` to the end.
3. Insert `item2` at index `3`.
4. Extend the list using its first three elements.
5. Pop the fifth element and store it in `popped_item`.
6. Remove the first occurrence of `item2`.
7. Replace the element at index `4` with `None`.
8. Replace all even-index elements with `None`.
9. Delete the third-last element.
10. Delete all even-index elements.

Return:

```python
(items, popped_item)
```

---

### 2. `list_non_mutating_operations(items, item1, item2)`

Perform the same logical operations **without modifying the original list**.

Return:

```python
items
```

---

### 3. `do_set_operation(set1, set2, set3, item1, item2)`

Perform the following set operations:

1. Add `item1` to `set1`.
2. Remove `item2` from `set1`.
3. Update `set1` using `set2`.
4. Remove all elements from `set1` that are also in `set3`.
5. Print the common elements of `set2` and `set3`.
6. Print the union of all three sets.
7. Print elements present in `set2` but not in `set3`.
8. Print the symmetric difference of `set2` and `set3`.

Return:

```python
(set1, sorted(set1), sorted(set2), sorted(set3))
```

---

# Solution

```python
def list_mutating_operations(items: list, item1, item2):

    # Sort the original list (in-place)
    items.sort()
    print("sorted:", items)

    # Add item1 at the end
    items.append(item1)
    print("append:", items)

    # Insert item2 at index 3
    items.insert(3, item2)
    print("insert:", items)

    # Extend using the first three elements
    items.extend(items[:3])
    print("extend:", items)

    # Remove the fifth element (index = 4)
    popped_item = items.pop(4)
    print("pop:", items)

    # Remove first occurrence of item2
    items.remove(item2)
    print("remove:", items)

    # Replace element at index 4 with None
    items[4] = None
    print("modify_index:", items)

    # Replace elements at even indices with None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:", items)

    # Delete third-last element
    del items[-3]
    print("delete_index:", items)

    # Delete elements at even indices
    del items[::2]
    print("delete_slice:", items)

    return items, popped_item


def list_non_mutating_operations(items: list, item1, item2):

    # Print sorted copy
    print("sorted:", sorted(items))

    # Append without modifying original list
    print("append:", items + [item1])

    # Insert item2 at index 3
    print("insert:", items[:3] + [item2] + items[3:])

    # Extend using first three elements
    print("extend:", items + items[:3])

    # Remove fifth element
    print("pop:", items[:4] + items[5:])

    # Remove first occurrence of item2
    if item2 in items:
        idx = items.index(item2)
        print("remove:", items[:idx] + items[idx+1:])
    else:
        print("remove:", items[:])

    # Replace index 4 with None
    temp = items[:]
    temp[4] = None
    print("modify_index:", temp)

    # Replace even indices with None
    temp = items[:]
    temp[::2] = [None] * len(temp[::2])
    print("modify_slice:", temp)

    # Delete even indices
    print("delete_slice:", items[1::2])

    return items


def do_set_operation(set1, set2, set3, item1, item2):

    # Add item1
    set1.add(item1)
    print(sorted(set1))

    # Remove item2 safely
    set1.discard(item2)
    print(sorted(set1))

    # Add all elements of set2
    set1.update(set2)
    print(sorted(set1))

    # Remove elements present in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # Common elements
    print(sorted(set2.intersection(set3)))

    # Union of all three sets
    print(sorted(set1.union(set2, set3)))

    # Elements in set2 but not in set3
    print(sorted(set2.difference(set3)))

    # Symmetric Difference
    print(sorted(set2.symmetric_difference(set3)))

    return set1, sorted(set1), sorted(set2), sorted(set3)
```

---

# Concepts Used

## List Mutating Methods

| Method | Description |
|---------|-------------|
| `sort()` | Sorts the list in-place |
| `append()` | Adds an element at the end |
| `insert()` | Inserts an element at a specific index |
| `extend()` | Adds elements of another iterable |
| `pop()` | Removes and returns an element |
| `remove()` | Removes the first occurrence |
| `del` | Deletes element(s) |
| Slice Assignment | Modifies multiple elements simultaneously |

---

## List Non-Mutating Techniques

Instead of changing the original list, create new lists using:

- `sorted()`
- List slicing
- List concatenation (`+`)

---

## Set Methods

| Method | Purpose |
|---------|----------|
| `add()` | Add one element |
| `discard()` | Remove safely (no error if missing) |
| `update()` | Add all elements of another set |
| `difference_update()` | Remove common elements |
| `intersection()` | Common elements |
| `union()` | All unique elements |
| `difference()` | Elements in first set only |
| `symmetric_difference()` | Non-common elements |

---