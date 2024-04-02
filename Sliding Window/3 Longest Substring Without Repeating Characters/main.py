class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        n = len(s)
        l = 0

        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxLen = max(maxLen, r-l+1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
                
        return maxLen
        