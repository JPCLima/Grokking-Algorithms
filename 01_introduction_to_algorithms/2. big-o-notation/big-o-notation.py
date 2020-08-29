import math

# Suppose you have a sorted list of 128 names, and you’re searching
# through it using binary search. What’s the maximum number of
# steps it would take?
# Max number Steps
print(math.log(128, 2))  # 7
print(math.log(128*2, 2))  # 8


# Note the running time increases as the list size increses
# The big O notations compare the number of operations, tells how fast the algorithm grows
# Big O notion  is the worst case scenario

# Binary search: O(log n)
# Simple search: O(n)
# Quicksort: O(n*log n)
# Selection Sort: O(n^2)
# Traveling salesperson Sort: O(n!)
