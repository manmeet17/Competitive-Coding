for i in range(int(input())):
    s=input().lower()
    n=len(s)
    for j in range(n):
        if s[j]=="n" and s[j+1]=="o" and s[j+2]=="t":
            if j+3<=n-1 and (s[j+3]=="" or s[j+3]==" "):
                if j-1>=0:
                    print("k")