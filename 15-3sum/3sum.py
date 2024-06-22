class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                     temp = [nums[i], nums[j], nums[k]]
                     ans.append(temp)
                     j += 1
                     k -= 1
                     while j<k and nums[j] == nums[j-1]:
                        j += 1
                     while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return ans

        