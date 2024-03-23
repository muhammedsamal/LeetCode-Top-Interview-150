class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i
        return res.lower() == res.lower()[::-1]
        