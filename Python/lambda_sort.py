a=[22,12,4,3,7,5,61,23,99,76,-2,54,33,0]
import functools
def cmp(x,y):
    # print(x,y)
    if (x%2==0 and y%2!=0) or (x<y and ((x%2==0 and y%2==0) or (x%2!=0 and y%2!=0))):
        return -1
    return 1

# l=functools.cmp_to_key(cmp)
# print(l)

print(sorted(a, key= functools.cmp_to_key(cmp)))
