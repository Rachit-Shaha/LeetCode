class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ele1, ele2 = float('-inf'), float('-inf')
        count1 = 0
        count2 = 0
        for i in range(n):
            if count1 == 0 and ele2 != nums[i]:
                count1 += 1
                ele1 = nums[i]
            elif count2 == 0 and ele1 != nums[i]:
                count2 += 1
                ele2 = nums[i]
            elif ele1 == nums[i]:
                count1 += 1
            elif ele2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        count1, count2 = 0, 0
        for i in range(n):
            if ele1 == nums[i]:
                count1 += 1
            if ele2 == nums[i]:
                count2 += 1
        if count1 > n//3:
            result.append(ele1)
        if count2 > n//3:
            result.append(ele2)
        return result

