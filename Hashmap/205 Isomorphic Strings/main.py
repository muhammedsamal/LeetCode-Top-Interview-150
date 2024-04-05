class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in sMap and sMap[c1] != c2) or
                (c2 in tMap and tMap[c2] != c1)):
                return False
            
            tMap[c2] = c1
            sMap[c1] = c2
        return True
        
        