def binsearch(array,key,low,high):
    if low>high:
        return -1
    mid=int((low+high)/2)
    if key==array[mid]:
        return mid
    elif key <array[mid]:
        high = mid-1
        return binsearch(array,key,low,high)
    else:
        low=mid+1
        return binsearch(array,key,low,high)

sortedarray=[10,5,12,15,20,31,34]
item= int(input("enter search item:"))
res=binsearch(sortedarray,item,0,len(sortedarray)-1)
if res>=0:
    print("found")
else:
    print("not found")