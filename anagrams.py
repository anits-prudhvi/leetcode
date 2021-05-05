def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = dict()
    for s in strs:
        k = "".join(sorted(s))
        if k in anagrams.keys():
            anagrams[k].append(s)
        else:
            anagrams[k] = [s]
    res = []
    for k in anagrams:
        res.append(anagrams[k])
    return res

def groupAnagrams_count(strs: list[str]) -> list[list[str]]:
        anagrams = dict()
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c) - ord('a') -1] +=1
            k = tuple(counts)
            if k in anagrams.keys():
                anagrams[k].append(s)
            else:
                anagrams[k] = [s]
        res = []
        for k in anagrams:
            res.append(anagrams[k])
        return res
m = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(m))
print(groupAnagrams_count(m))
