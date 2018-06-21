class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in xrange(0, len(nums)):
            num = nums[i]
            if num in d:
                return[d[num], i]
            else:
                d[target-num] = i
        return None
