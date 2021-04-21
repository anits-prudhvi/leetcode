def addBinary(a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        res = ""
        while i >= 0 and j >= 0:
            print(i, j, res)
            if a[i] == '1':
                if b[j] == '1':
                    if c == 0:
                        c = 1
                        res = str(0) + res
                    else:
                        c = 1
                        res = str(1) + res
                else:
                    if c == 0:
                        c = 0
                        res = str(1) + res
                    else:
                        c = 1
                        res = str(0) + res
            else:
                if b[j] == '1':
                    if c == 0:
                        c = 0
                        res = str(1) + res
                    else:
                        c = 1
                        res = str(0) + res
                else:
                    if c == 0:
                        c = 0
                        res = str(0) + res
                    else:
                        c = 0
                        res = str(1) + res
            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == '0' and c == 0:
                res = str(0) + res
            elif a[i] == '0' and c == 1:
                res = str(1) + res
                c = 0
            elif a[i] == '1' and c == 0:
                res = str(1) + res
            elif a[i] == '1' and c == 1:
                res = str(0) + res
                c = 1
            print(i, j, c, res)
            i -= 1
        while j >= 0:
            if b[j] == '0' and c == 0:
                res = str(0) + res
            elif b[j] == '0' and c == 1:
                res = str(1) + res
                c = 0
            elif b[j] == '1' and c == 0:
                res = str(1) + res
            elif b[j] == '1' and c == 1:
                res = str(0) + res
                c = 1
            print(i, j, c, res)
            j -= 1

        if c == 0:
            return res
        else:
            return str(1) + res

print(addBinary("11","1"))