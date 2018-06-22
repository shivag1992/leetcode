class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(s == ""):
            return True
        paren_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s:
            stack.append(char)
            if char in paren_map.keys():
                if(len(stack) == 1):
                    return False
                if(paren_map[char] == stack[-2]):
                    stack.pop()
                    stack.pop()
                else:
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False
