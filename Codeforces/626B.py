input()
s = input()
rc = s.count('R')
gc = s.count('G')
bc = s.count('B')

rc = 2 if rc > 1 else rc
gc = 2 if gc > 1 else gc
bc = 2 if bc > 1 else bc

ans = ''

if gc == bc == 0 or gc*bc > 0 or (gc*bc == 0 and gc+bc>1 and rc > 0):
    ans = ans+'R' 
if rc == bc == 0 or rc*bc > 0 or (rc*bc == 0 and rc+bc>1 and gc > 0):
    ans = ans+'G' 
if gc == rc == 0 or gc*rc > 0 or (gc*rc == 0 and gc+rc>1 and bc > 0):
    ans = ans+'B' 

print(''.join(sorted(set(ans))))
