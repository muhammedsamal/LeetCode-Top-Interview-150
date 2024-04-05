# <a href="https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150">383 Random Note</a>

### Description

> Tags: *Hash Table, String, Counting*

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

 

Example 1:
```
Input: ransomNote = "a", magazine = "b"
Output: false
```
Example 2:
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```
Example 3:
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

> Understand the problem

1. len(magazine) >= len(ransomNote) 
1. each letter can be only used once, therefore we need letter count

> Drawings



> to code

- built a hashmap for frequency counts
- compare the letter frequency in both ransomNote and magazine