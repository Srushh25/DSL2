def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return(arr,low,mid-1,x)
        else:
            return(arr,mid+1,high,x)
    else:
        return -1
arr=[2,5,10,21,34]
x=21
result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element present at ",str(result))
else:
    print("Element not present ")
