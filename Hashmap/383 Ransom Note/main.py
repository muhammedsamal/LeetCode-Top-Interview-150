class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = Counter(ransomNote), Counter(magazine)

        return note & mag == note