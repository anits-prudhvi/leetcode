
def validPalindrome(s: str) -> bool:
        l = len(s) -1
        i = 0
        j = l
        while i < j:
            print(i, j, s[i], s[j])
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if validPalindrome(s[i+1:j+1]) or validPalindrome(s[i:j]):
                    return True
                else:
                    return False
        return True

print(validPalindrome("ebcbbececabbacecbbcbe"))