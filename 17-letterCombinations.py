class Solution(object):
    def __init__(self):
        self.d = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        if digits in self.d:
            return self.d[digits]
        l = []
        l1 = self.letterCombinations(digits[0:len(digits) - 1])
        l2 = self.letterCombinations(digits[-1])
        for i in xrange(0, len(l1)):
            for j in xrange(0, len(l2)):
                l.append(l1[i] + l2[j])
        self.d[digits] = l
        return l
