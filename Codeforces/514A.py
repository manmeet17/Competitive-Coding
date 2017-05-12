v=[min(int(x),9-int(x)) for x in input()]
if v[0]<1:v[0]=9
print(''.join(map(str,v)))
