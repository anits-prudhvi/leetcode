def merge(nums1,n,nums2,m):
    t,t1 = 0
    i,j = 0
    while i < n and j < m:
        if nums1[i] > nums2[j]:
            if t==0:
                t = nums1[i]
                i += 1
                j += 1
            else:
                if t < nums2[j]:
                    t1 = nums1[i]
                    nums1[i] = t
                    