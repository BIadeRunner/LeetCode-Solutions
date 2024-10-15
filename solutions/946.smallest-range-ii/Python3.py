class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_score = nums[-1] - nums[0]
        
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i+1] - k)
            min_score = min(min_score, high - low)
        
        return min_score