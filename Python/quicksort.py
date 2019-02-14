def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    j=low
    while j<high:
        print("Current--->",arr[j])
        print("Changed--->",arr)

        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    print("I--->",i+1)
    arr[i+1],arr[high]= arr[high],arr[i+1]
    print("Final--->",arr)
    return i+1


def quicksort(arr, low, high):
    if low<high:
        print(arr)
        pi=partition(arr,low,high)
        print(pi,arr,"\n\n")
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr=[5,3,4,1,6,2]
quicksort(arr,0,len(arr)-1)
print(arr)