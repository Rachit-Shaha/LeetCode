class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ele = None
        count = 0
        for i in range(n):
            if count == 0:
                count = 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -= 1
        return ele
            
        