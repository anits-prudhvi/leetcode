
def numUniqueEmails(emails: list[str]) -> int:
        res = set()
        for i in emails:
            if '+' in i:
                zj = i.index("@")
                t1 = i[:zj].replace(".","")
                zi = t1.index("+")
                t = t1[:zi] + i[zj:]
                #t.replace(".","")
                res.add(t)
            else:
                zj = i.index("@")
                t = i[:zj].replace(".","") + i[zj:]
                res.add(t)
        return len(res)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(numUniqueEmails(emails))
