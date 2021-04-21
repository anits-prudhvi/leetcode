def maxArea(height: list[int]) -> int:
        max_area = -1
        i = 0
        j = len(height) - 1
        while i < j:
            #print(i,j)
            area = (j - i) * (min(height[i],height[j]))
            if max_area < area:
                max_area = area
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area

height = [1,8,6,2,5,4,8,3,7]
height = [4,3,2,1,4]
print(maxArea(height))