class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 1
        for i in range(1, n):
            if nums[i-1] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p
        