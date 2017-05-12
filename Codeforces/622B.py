s = input()
h = int(s[0:2])
m = int(s[3:5])
allmin = 60 * h + m;
allmin += int(input())

allmin = allmin % (24 * 60)

h = allmin//60;
m = allmin % 60
print ("%02d:%02d" %(h,m))
