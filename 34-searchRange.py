class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.binary_search(nums, target, first=True)
        end = self.binary_search(nums, target, first=False)
        return [start, end]
    
    def binary_search(self, nums, target, first):
        l = 0
        h = len(nums) - 1
        ans = -1
        while(l <= h):
            mid = l + (h - l )/2
            if(target == nums[mid]):
                if first:
                    h = mid - 1
                else:
                    l = mid + 1
                ans = mid
            if(target > nums[mid]):
                l = mid + 1
            elif(target < nums[mid]):
                h = mid - 1
        return ans
