for i in range(int(input())):
    s=input()
    n=int(input())
    l=len(s)
    if n==1:
        print (s)
        continue
    row=0
    arr=["" for x in range(l)]
    down=True
    for j in range(l):
        arr[row]+=s[j]
        if row==0:
            down=True
        elif row==n-1:
            down=False
        if down==True:
            row+=1
        else:
            row-=1
    for j in arr:
        print (j,end='')
    print()
