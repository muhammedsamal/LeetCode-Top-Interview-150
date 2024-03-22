class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = [""]*numRows
        count = 0
        steps = 1
        for letter in s:
            if count == numRows-1:
                steps = -1
            elif count == 0:
                steps = 1
            res[count] += letter
            count += steps
        return "".join(res)