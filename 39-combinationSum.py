class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.helper(candidates, target, 0, [], results)
        return results
    
    def helper(self, candidates, target, start, soFar, results):
        if(sum(soFar) == target):
            results.append(soFar)
            return
        if(start>=len(candidates)):
            return
        if(sum(soFar)>=target):
            return
        self.helper(candidates, target, start, soFar + [candidates[start]], results)
        self.helper(candidates, target, start + 1, soFar, results)
