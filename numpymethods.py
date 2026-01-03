from numpy import *
# here typecode is not neccessary
# numpy gives the facility to create a heterogeneous array 
val = array([1,2,4,'s'])

for x in val:
    print(x,end=" ")

print("\n")
# array creation automatically using linspace
# in line space start and end will be inclusive
val2 = linspace(10,20,5)

for x in val2:
    print(x,end=" ")

print("\n")
#  here start will be inclusive but the end will be exclusive
val3 = arange(10,20,2)

for x in val3:
    print(x,end=" ")

print("\n")

val4 = logspace(10,20,2)

for x in val4:
    print(x,end=" ")

print("\n")
# when you want all the element to be same 
val5 = ones(10)

for x in val5:
    print(x,end=" ")

# specific size and the default values

val6 = full(10,5)

for x in val6:
    print(x,end=" ")



