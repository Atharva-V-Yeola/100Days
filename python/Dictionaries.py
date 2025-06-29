# Dictionaries in Python are equivalent to Maps in C++/JAVA. They are used to store
# data in key-value pairs.
# Printing key and values in dictionaries:
# To print the keys of the dictionary, use the .keys() method and to print the values, use
# .values() method.

di = {'fir': 'one','sec':'2','thr':'thi'}
# for key in di.keys():
#     print(key)
# for value in di.values():
#     print(value)

# Update key value in dictionary:
# Update key value which is not present in dictionary:
# We can update a key value in a dictionary by accessing the key withing [] and
# setting it to a value.

# di['fourth'] = '4'
# for item in di.items():
#     print(item)

# Update key value which is present in the dictionary:
# We can update a key value in a dictionary, when the key is present in the exact
# same way as we update a key, when the key is not present in the dictionary.

# di['thr'] = '3'
# for i in di.items():
#     print(i)

# Delete key-value pair from dictionary:
# We can delete a key-value pair from a dictionary using the del keyword followed
# by the key value to be deleted enclosed in [].

# del di['thr']
# for i in di.items():
#     print(i)

# Merging 2 dictionaries
# We can merge 2 dictionaries into 1 by using the update() method.

dict1 = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
dict2 = {1: 3, 2: 4, 3: 5}
dict1.update(dict2)
print(dict1)

