def numDecodings(s: str) -> int:
        if s[0] == '0':
            return 0
        oneback = 1
        twoback = 1
        for i in range(1,len(s)):
            current = 0
            if s[i] != '0':
                current = oneback
            t = int(s[i-1:i+1])
            if  t >= 10 and t <= 26:
                    current += twoback
            twoback = oneback
            oneback = current
        return oneback

def test_num(s):
    if s[0] == "0":
        return 0

    two_back = 1
    one_back = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0":
            current = one_back
        two_digit = int(s[i - 1: i + 1])
        if two_digit >= 10 and two_digit <= 26:
            current += two_back
        two_back = one_back
        one_back = current

    return one_back
print(test_num("2101"))
print(numDecodings("2101"))