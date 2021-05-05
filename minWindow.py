def minWindow(s: str, t: str) -> str:
        i=0
        j = i + len(t) -1
        n = len(s)
        length = 10**5
        window = ""
        #print(i,j)
        while j < n and i+len(t)-1 < n:
            flag = 0
            for c in t:
                if c in s[i:j+1]:
                    continue
                else:
                    flag += 1
            if flag == 0:
                if j-i+1 < length:
                    length = j -i +1
                    window = s[i:j+1]
                i += 1
            else:
                j += 1

        return window

s = "aa"
t = "aa"
print(minWindow(s,t))

