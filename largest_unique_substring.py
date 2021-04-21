def lengthOfLongestSubstring(s: str) -> int:
        max = -1
        hash_slide = dict()
        j =0
        i =0
        n = len(s)
        while i < n:
            if s[i] in hash_slide:
                t = len(hash_slide)
                if max < t:
                    max = t
                if s[j] == s[i] and j != -1:
                    hash_slide[s[i]] = i
                    j += 1
                    i += 1
                else:
                    hash_slide.pop(s[j])
                    j += 1
            else:
                hash_slide[s[i]] = i
                i += 1
        t = len(hash_slide)
        if max < t:
            return t
        else:
            return max
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
        max = -1
        hash_slide = dict()
        j = 0
        i = 0
        n = len(s)
        t = 0
        while i < n:
            if s[i] in hash_slide:
                    hash_slide[s[i]] += 1
                    i += 1
                    t += 1
            else:
                if len(hash_slide) == 2:
                    if hash_slide[s[j]] == 1:
                        hash_slide.pop(s[j])
                    else:
                        hash_slide[s[j]] -=1
                    j += 1
                    t -= 1
                else:
                    hash_slide[s[i]] = 1
                    i += 1
                    t += 1
            if max < t:
                max = t
        return max

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
        max = -1
        hash_slide = dict()
        j = 0
        i = 0
        n = len(s)
        t = 0
        while i < n:
            if s[i] in hash_slide:
                hash_slide[s[i]] += 1
                i += 1
                t += 1
            else:
                if len(hash_slide) == k:
                    if hash_slide[s[j]] == 1:
                        hash_slide.pop(s[j])
                    else:
                        hash_slide[s[j]] -= 1
                    j += 1
                    t -= 1
                else:
                    hash_slide[s[i]] = 1
                    i += 1
                    t += 1
            if max < t:
                max = t
        return max

#s = "bbbbb"
s = "abcabcbb"
#s = "pwwkew"
#s = "eceba"
#print(lengthOfLongestSubstring(s))
#print(lengthOfLongestSubstringTwoDistinct(s))
print(lengthOfLongestSubstringKDistinct(s,3))
