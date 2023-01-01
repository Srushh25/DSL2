l1=[5,4,3,2,1]
l2=[5,4,3,2,1]
size=5
def bubble_sort():
    print("List - ",l1)
    i=j=0
    for i in range(size-1):
        for j in range(size-1):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
        print("Pass ",i+1,l1)
bubble_sort()

def selection_sort():
    print("List - ",l2)
    i=0
    for i in range(size-1):
        j=i+1
        while j<size:
            if l2[i]>l2[j]:
                temp=l2[i]
                l2[i]=l2[j]
                l2[j]=temp
                j+=1
        print("Pass ",i+1,l2)
selection_sort()
    
