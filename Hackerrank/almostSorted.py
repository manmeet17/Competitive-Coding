# Complete the almostSorted function below.
def isSort(arr,arr2):
    return arr==arr2

def almostSorted(arr,n):
    sort=sorted(arr)
    if arr==sort:
        return ["yes"]
    i=0
    while arr[i]<arr[i+1]:
        i+=1
    a=i
    # print("A---->",a)
    while i<n-1 and arr[i]>arr[i+1]:
        i+=1
    # print("I rev---->",i)
    temp=arr[:a]+list(reversed(arr[a:i+1]))+arr[i+1:]
    # print("Temp---->",temp)
    if isSort(sort,temp):
        if (i-a)==1:
            return ("yes","swap",a+1,i+1)
        return ("yes","reverse",a+1,i+1)
    i=a+1
    while i<n-1 and  arr[i]<arr[i+1]:
        i+=1
    if i==n-1:
        return ["no"]
    # print("I swap---->",i)    
    arr[a],arr[i+1]=arr[i+1],arr[a]
    # print("Temp swap---->",arr)
    if isSort(sort,arr):
        return ("yes","swap",a+1,i+2)
    return ["no"]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    ans = almostSorted(arr,n)
    if len(ans)==1:
        print(ans[0])
    else:
        print(ans[0])
        print(ans[1], ans[2], ans[3])
