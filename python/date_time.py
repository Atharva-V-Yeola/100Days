#time class: We can represent time values using the time class.
# import datetime
# a = datetime.time(3,58,45,10)
# print(a)

#date class: We can represent date values using the date class.
# import datetime
# date = datetime.date(2000, 11, 16)
# print('Date date is ', date.day, ' day of ', date.month, ' month of the year ', date.year)

# Conversion from date to time: We can convert a date to its corresponding time
# using the strptime() function.
# from datetime import datetime
# print(datetime.strptime('20/02/2025','%d/%m/%Y'))

#print(datetime.now())

# time.strfime() in Python: It converts a tuple or struct_time representing the
# time into a string object.
from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
print(s)