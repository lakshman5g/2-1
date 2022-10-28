#from math import *
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = []
n=int(input("Enter the size of the array:"))
print("Enter elements into the array:")
for i in range(n):
    ele=int(input())
    arr.append(ele)
key=int(input("Enter the key element: "))
print("element found at index "+str(linearsearch(arr,key)))