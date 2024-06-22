class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int):
        merged = []
        left = low
        right = mid+1
        while(left<=mid and right<=high):
            if nums[left] <= nums[right]:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1
        while (left <= mid):
            merged.append(nums[left])
            left += 1
        while (right <=high):
            merged.append(nums[right])
            right += 1
        for i in range(low, high+1):
            nums[i] = merged[i-low]

        
    def countPairs(self, nums: List[int], low: int, mid: int, high) -> int:
        cnt = 0
        right = mid + 1
        for i in range(low, mid +1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += (right - (mid+1))
        return cnt


    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid+1, high)
        cnt += self.countPairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return cnt


    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)
        