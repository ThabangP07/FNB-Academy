# ---------- SETS ----------

# Sets are unordered collections of unique elements.

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}    

# Adding elements to a set
my_set.add(6)  # Add a single element

# Removing elements from a set
my_set.remove(2)  # Remove a specific element       
print(my_set)  # Output: {1, 3, 4, 5, 6}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)  # or set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set1.intersection(set2)  # or set1 & set2    
print(intersection_set)  # Output: {3}

# Difference of two sets
difference_set = set1.difference(set2)  # or set1 - set2    
print(difference_set)  # Output: {1, 2}

# Symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)  # or set1 ^ set 2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}