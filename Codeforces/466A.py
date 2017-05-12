import math
s=list(map(int,input().split()))
print (min(s[0]*s[2],(s[3]*int(s[0]/s[1]))+(s[0]%s[1])*s[2],int(math.ceil(s[0]/s[1]))*s[3]))
