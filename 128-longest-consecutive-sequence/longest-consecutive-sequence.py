class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        set_nums = set(nums)
        n = len(set_nums)
        for i in set_nums:
            if i - 1 not in set_nums:
                cnt = 1
                temp = i
                while temp + 1 in set_nums:
                    cnt += 1
                    temp += 1
                longest = max(longest, cnt)
        return longest

        