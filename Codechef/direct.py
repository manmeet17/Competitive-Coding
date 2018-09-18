for _ in range(int(input())):
    n=int(input())
    loc=[]
    di=[]
    for i in range(n):
        s=input().split()
        d=s[0]
        place=s[2:]
        if d=="Begin":
            loc.append(place)
        else:
            if d=="Left":
                di.append("Right")
            else:
                di.append('Left')
            loc.append(place)
    print("Begin on "+(' '.join(loc.pop())))
    for i in range(n-1):
            print( di.pop()+" on "+(' '.join(loc.pop())))