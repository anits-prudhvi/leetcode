def twoSum(nums_hash: list[int], target: int, ignore: int) -> list[int]:
        res = []
        for i in nums_hash:
            if len(nums_hash[i]) == 1 and nums_hash[i][0] == ignore:
                continue
            d = target - i
            if d in nums_hash.keys():
                if i == d :
                    if len(nums_hash[i]) == 1:
                        continue
                    if ignore in nums_hash[d] and len(nums_hash[d]) > 2:
                        res.append([i,d])
                elif len(nums_hash[d]) == 2 and ignore in nums_hash[d]:
                        continue
                if len(nums_hash[d]) == 1 and ignore in nums_hash[d]:
                    continue
                else:
                    res.append([i,d])
        return res

def threeSum(nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums_hash = dict()
        for i in range(n):
            if nums[i] in nums_hash:
                nums_hash[nums[i]].append(i)
            else:
                nums_hash[nums[i]] = [i]
        res = set()
        for i in range(n):
            r = twoSum(nums_hash,(0-nums[i]),i)
            if r == []:
                continue
            else:
                for e in r:
                    t = [nums[i],e[0],e[1]]
                    t.sort()
                    res.add(tuple(t))
        re = []
        for i in res:
            re.append(list(i))
        return re

nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
nums = [-1,0,1,0]
#nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
