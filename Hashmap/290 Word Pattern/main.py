class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sMap = {}
        tMap = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            c1, c2 = pattern[i], s[i]

            if ((c1 in sMap and sMap[c1] != c2) or
                (c2 in tMap and tMap[c2] != c1)):
                return False
            
            tMap[c2] = c1
            sMap[c1] = c2
        return True