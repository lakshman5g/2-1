def partition(a,l,h):
    p=a[h]
    i=l-1
    for j in range(l,h):
        if p>=a[j]:
            i+=1
        a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def quick(a,low,high):
   if low<high:
       p=partition(a,low,high)
       quick(a,low,p-1)
       quick(a,p+1,high)
a=[5,2,15,10,6]
quick(a,0,len(a)-1)
print(a)