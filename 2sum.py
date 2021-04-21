
def twoSum(nums: list[int], target: int) -> list[int]:
        h = dict()
        for i in range(0,len(nums)):
            if (target-nums[i]) in h.keys():
                r_i = h[target-nums[i]]
                if i != r_i:
                    return [i,r_i]
            else:
                h[nums[i]] = i


nums = [3,2,4]
target = 6

print(twoSum(nums,target))