inp='*|*****|*|***|*'
s=[]
e=[]
lookup = []
for i in range(0,len(s)):
    if s[i] == '|':
        lookup.append(i)
min = lookup[0]
max = lookup[-1]
for i,j in s,e:
    if i
