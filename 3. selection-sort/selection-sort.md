# Selection Sort

> This algorithim takes a O(n*n) time

Selection Sort is not very fast, The Quicksort is a faster sorting algorithm, takes O(n log n)

- Create a function to find the smallest element
```python
  def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
```


- Create a function to sort the the array from the samllest to the largest 