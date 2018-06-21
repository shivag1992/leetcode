class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        ans = None
        for i in xrange(0, numRows):
            row_str = None
            dir = False
            j = i
            if i == 0 or i == (numRows - 1):
                while j < len(s):
                    remRows = numRows -1
                    inc = 2 * remRows
                    if row_str is None:
                        row_str = s[j]
                    else:
                        row_str = row_str + s[j]
                    j = j + inc
                if ans is None:
                    ans = row_str
                else:
                    ans = ans + row_str
                continue
            while j < len(s):

                if row_str is None:
                    row_str = s[j]
                else:
                    row_str = row_str + s[j]
                dir = not dir
                remRows = (numRows -1) - i if dir else i
                inc = 2 * remRows
                j = j + inc
            if ans is None:
                ans = row_str
            else:
                ans = ans + row_str
        return ans
