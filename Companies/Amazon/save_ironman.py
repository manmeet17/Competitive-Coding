for i in range(int(input())):
    s=input()
    a=0
    b=len(s)-1
    f=1
    while(a<=b and a<len(s)):
        # print (a,b)
        if (ord(s[a]) not in list(range(65,91)) and ord(s[a]) not in list(range(48,58))) and (ord(s[a])<97 or ord(s[a])>122):
            a+=1
            continue
        if (ord(s[b]) not in list(range(65,91)) and ord(s[b]) not in list(range(48,58))) and (ord(s[b])<97 or ord(s[b])>122):
            b-=1
            continue
        # print (s[a],s[b])
        if(s[a].lower()!=s[b].lower()):
            f=0
            break
        a+=1
        b-=1
    print ("YES" if f else "NO")
