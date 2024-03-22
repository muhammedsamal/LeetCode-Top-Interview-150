class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        f = strs[0]
        l = strs[-1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return res
            res += f[i]
        return res
        