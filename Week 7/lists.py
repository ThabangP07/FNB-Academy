# ----------lISTS----------
# This is a simple list of fruits

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

fruits[1] = "blueberry"  # Change banana to blueberry
print(fruits)

# list methods

fruits.append("orange")  # Add orange to the end of the list
print(fruits)

fruits.insert(1, "kiwi")  # Insert kiwi at index 1
print(fruits)

fruits.remove("cherry")  # Remove cherry from the list
print(fruits)