# Lists are used to store multiple items in a single variable.
eg = ['Sum','Mon','Tue','Wed','Thus']
print(eg)
#accessing elements using zero based indexing
print(eg[0],eg[1])
#negative indexing starts from -1
print(eg[-1])
#slicing
print(eg[2:4])
print(eg[-5:-1])
#replace
eg[0] = 'Friday'
print(eg)

#concatination
es = ['now','then']
ap = es+eg
print(ap)
#replication
tre = es*3
print(tre)
#delete
del eg[4]
print(eg)

#looping
for e in tre:
    print(e)

# in and in not
print('Sun' in eg)
print('Sun' not in eg)

#adding values
# insert - This function inserts an element into a particular index of a list.
eg.insert(1,'Sun')
print(eg)

#append - This function appends an element at the back of a list.
eg.append('Days')
print(eg)

#sorting a list
eg.sort()
print(eg)
eg.sort(reverse=True)
print(eg)

