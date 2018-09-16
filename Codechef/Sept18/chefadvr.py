for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    if n>=2 and m>=2:
        if ((n-1)%x==0 and (m-1)%y==0) or ((n-2)%x==0 and (m-2)%y==0):
            print ('Chefirnemo')
        else:
            print("Pofik")
    else:
        if (n==m) or (n==1 and (m-1)%y==0) or (m==1 and (n-1)%x==0):
            print ('Chefirnemo')
        else:
            print ("Pofik")
