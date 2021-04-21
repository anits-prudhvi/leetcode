def longestCommonPrefix(strs: list[str]) -> str:
    def recursive_match(s1, s2):
        if type(s2) == list and len(s2) > 1:
            return recursive_match(s1,recursive_match(s2[0], s2[1:]))
        else:
            if len(s2) == 1:
                s2 = s2[0]
            print(s1, s2)
            t = len(s2)
            while (s1[0:t] != s2[0:t]):
                t -= 1
            if t == -1:
                return ""
            else:
                return s2[0:t]

    #print(strs)
    if len(strs) == 1:
        return strs[0]
    elif len(strs) == 0:
        return ""
    else:
        return recursive_match(strs[0], strs[1:])

strs = ["reflower","flow","flight"]

print(longestCommonPrefix(strs))