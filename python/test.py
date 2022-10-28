def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
def recursive_la(l,current_index,x):
    if current_index<0:
        return -1
    if l[current_index]==x:
        return current_index
    else:
        return recursive_la(l,(current_index)-1,x)
a=[]
n=int(input("Enter size of the array:"))
print("Enter the array elements:")
for i in range(n):
    ele=int(input())
    a.append(ele)
key=int(input("Enter the key value: "))
print("Element found at the index: ",linearsearch(a,key))
print("Element found at the index: ",recursive_la(a,len(a)-1,key))