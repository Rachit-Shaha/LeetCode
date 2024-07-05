class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = [-1] * 256
        left = 0
        right = 0
        n = len(s)
        answer = 0
        while right < n:
            if d[ord(s[right])] != -1:
                left = max(d[ord(s[right])] + 1, left)
            d[ord(s[right])] = right
            answer = max(answer, right - left + 1)
            right += 1
        return answer
        