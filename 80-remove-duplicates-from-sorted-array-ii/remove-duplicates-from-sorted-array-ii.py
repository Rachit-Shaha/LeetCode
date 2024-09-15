class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 1
        r = 1
        count = 1
        while l < len(nums):
            if nums[l] == nums[l-1]:
                count += 1
                if count > 2:
                    l += 1
                    continue
            else:
                count = 1
            nums[r] = nums[l]
            r += 1
            l += 1
        return r

        