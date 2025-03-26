class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        curr_sum = 0

        for i in range(k):
            curr_sum+= nums[i]

        max_avg = curr_sum/ k

        for i in range(k, len(nums)):
            curr_sum+= nums[i]
            curr_sum-= nums[i-k]

            avg = curr_sum/ k
            max_avg = max(max_avg, avg)

        return max_avg

        