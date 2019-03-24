nums=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

h=int(input())
m=input()

if m=='00':
    print(nums[h],"o' clock")
elif int(m)==1:
    print(nums[int(m)],'minute past',nums[h])
elif m=='15':
    print(nums[int(m)],'past',nums[h])
elif m=='30':
    print('half past',nums[h])
elif int(m)<30:
    print(nums[int(m)],'minutes past',nums[h])
elif m=='45':
    print(nums[60-int(m)],'to',nums[h+1])
elif m=='59':
    print(nums[60-int(m)],'minute to',nums[h+1])
else:
    print(nums[60-int(m)],'minutes to',nums[1+h])
