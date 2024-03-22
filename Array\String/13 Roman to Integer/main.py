class Solution:
    def romanToInt(self, s: str) -> int:
        charMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = charMap[s[-1]] # iterate backwards
        for i in range(len(s) - 2, -1, -1):
            if charMap[s[i]] >= charMap[s[i+1]]:
                res += charMap[s[i]]
            else:
                res -= charMap[s[i]]
        
        return res