# List Comprehensions:
# It is a shorter syntax to create a new list using values of an existing list.
a = [1,2,3,4]
b = [i+1 for i in a]
print(b)

# Set Comprehension:
# It is a shorter syntax to create a new set using values of an existing set.
a = {9,8,7,6}
b = [i**2 for i in a]
print(b)

# Dict Comprehension:
# It is a shorter syntax to create a new dictionary using values of an existing
# dictionary.

d = {'Hello':'World','for':1}
c = {val : k for k, val in d.items()}
print(c)