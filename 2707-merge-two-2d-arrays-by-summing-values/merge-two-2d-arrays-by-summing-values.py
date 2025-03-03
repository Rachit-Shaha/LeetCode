class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        x = min(m, n)
        l = 0
        r = 0
        res = []

        while l < m and r < n:
            if nums1[l][0] == nums2[r][0]:
                res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                res.append([nums1[l][0], nums1[l][1]])
                l += 1
            else:
                res.append([nums2[r][0], nums2[r][1]])
                r += 1
        while l < m:
            res.append([nums1[l][0], nums1[l][1]])
            l += 1
        while r < n:
            res.append([nums2[r][0], nums2[r][1]])
            r += 1
        return res
        