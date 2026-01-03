# import array as arr
from array import *
val = array('i',[1,2,3,4,5,6,7,8])

for i in range(0,len(val)):
    print(val[i],end=" ")

print("\n")
# enhanced for loop here we don't have to worry about the array size
for x in val:
    print(x,end=' ,')
# finding the type code
print("\n")
print(val.typecode)
# reversing the array
print("\n")
val.reverse()
for i in range(0,len(val)):
    print(val[i],end=" ") 
print("\n")
# for inserting at the specific positionf
val.insert(1,50)
for i in range(0,len(val)):
    print(val[i],end=" ") 

# making a duplicate array for this we have two enter twp parameters typecode and bring all the element from the orginal array

copyArray = array(val.typecode,val)
print(copyArray[i],end=" ")
''' pop method used to delete the element of array 
 pop(index) to delete that index of element 
if you dont enter the index then bydefault behaviour is to delete the last element '''
# remove function require the values 
# slicing concept in python
# [start index: end index] staring index will be inclusive and ending index will be exclusive
val = array('i',[1,2,3,4,5,6,7,8,9])
abc = val[2:5]
for i in range(0,len(abc)):
    print(abc[i],end=" ")








