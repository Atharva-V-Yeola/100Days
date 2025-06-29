
# ------------------- for loop -------------------
# This loop format will iterate overall numbers from 0 to Limit - 1.
# for i in range(5):
#     print(i)

# ------------------  for with range(start,stop,step) -------------
# for i in range(2,10,2):
#     print(i)
# eq = [100,200,2400,300]
# total = 0
# for item in eq:
#     total+=item

# print(total)

eq = [100,200,2400,300]
total = 0
for i in range(len(eq)):
    print((i+1),'eq is',eq[i])
    total += eq[i]

print(total)
# -----------------  for with in ----------
# this is used to iterate  elements in lists, tuple, dictionary 

# a = [1,2,3,4,'Priyal']
# for ele in a:
#     print(ele)

#  ----------    while loop -------------
# cnt = 10
# while cnt>0:
#     print(cnt)
#     cnt-=1
