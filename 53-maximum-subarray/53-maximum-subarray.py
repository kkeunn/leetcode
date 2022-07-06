class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            local_sum  = max(local_sum + nums[i], nums[i])
            max_sum = max(local_sum, max_sum)
        return max_sum