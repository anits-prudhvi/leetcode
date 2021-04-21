
def subdomainVisits(cpdomains: list[str]) -> list[str]:
        counts = dict()
        for i in cpdomains:
            count_data = i.split(" ")
            domains = count_data[1].split(".")
            k = counts.keys()
            if ".".join(domains) in k:
                counts['.'.join(domains)] += int(count_data[0])
            else:
                counts['.'.join(domains)] = int(count_data[0])
            t = len(domains)
            for i in range(1,t):
                k = ".".join(domains[i:t])
                if k in counts.keys():
                    counts[k] += int(count_data[0])
                else:
                    counts[k] = int(count_data[0])
        result = []
        for i in counts.keys():
            result.append(str(counts[i]) + " " + str(i))
        return result


inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(inp))