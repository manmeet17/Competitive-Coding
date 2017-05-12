a,b,s = map(int, input().split())
print('Yes' if (s >= abs(a) + abs(b) and (s - (a + b)) % 2 == 0) else 'No')
