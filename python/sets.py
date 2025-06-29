# Sets are initialized using curly braces {} or set() in python.
# A python set is basically an unordered collection of unique values, i.e. it will
# automatically remove duplicate values from the set.

# s = {1, 2, 3}
# print(s)
# s = set([1, 2, 3])
# print(s)
# s = {1, 2, 3, 3, 2, 4, 5, 5}
# print(s)

# Inserting elements in set:
# We can insert a single element into a set using the add function of sets.
# s = {1, 2, 3, 3, 2, 4, 5, 5}
# print(s)
# Insert single element
# s.add(6)
# print(s)

# To insert multiple elements into a set, we use the update function and pass a list of
# elements to be inserted as parameters.

# s.update([7,8,9])
# print(s)

# Deleting elements from the set:
# We can delete elements from a set using either the remove() or the discard()
# function.

# s.remove(3)
# print(s)
# s.discard(9)
# print(s)

#Operations in set
a = {1, 2, 3, 3, 2, 4, 5, 5}
b = {4, 6, 7, 9, 3}
# Performs the Intersection of 2 sets and prints them
print(a & b)
# Performs the Union of 2 sets and prints them
print(a | b)
# Performs the Difference of 2 sets and prints them
print(a - b)
# Performs the Symmetric Difference of 2 sets and prints them
print(a ^ b)