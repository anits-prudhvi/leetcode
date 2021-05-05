'''If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.'''

def compareVersion(version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l=[]
        for i,j in v1,v2:
            if int(i) > int(j):
                l.append('g')
                continue
            if int(i) < int(j):
                l.append('l')
                continue
            if int(i) == int(j):
                l.append('e')
                continue
        if l[0] == 'l':
            return -1
        for i in range(1,len(l)):
            if l[i-1] == 'e' and l[i] == 'l':
                return -1
            if l[i-1] == 'g' and l[i] == 'l':
                return 1
            if l[i-1] == 'e' and l[i] == 'g':
                return 1
        return 0

version1 = "0.1"
version2 = "1.1"
print(compareVersion(version1,version2))

