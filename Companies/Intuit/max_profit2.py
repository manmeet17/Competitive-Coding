for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    ans=[]
    for j in range(n-1):
        if l[j+1]>l[j]:
            a+=1
            if j==n-2:
                ans.append((j+1-a,j+1))
        else:
            ans.append((j-a,j))
            a=0
    f=0
    for j in ans:
        if j[0]!=j[1]:
            f=1
            print ("("+str(j[0])+" "+str(j[1])+")",end=' ')
    if(f==0):
        print ("No Profit")
        continue
    print()
