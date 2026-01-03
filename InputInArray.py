from array import *
arr = array('i',[])
n = int(input("enter the size of the array"))

for i in range (0,n):
    arr.append(int(input("enter the next input")))

for x in arr:
    print(x,end=" ")