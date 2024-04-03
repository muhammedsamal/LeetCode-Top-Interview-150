# <a href="https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150">14 Longest Common Prefix</a>

### Description

> Tags: *String, Trie*

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```
  
> Understand the problem

1. there can be test cases with no common prefix - return `""`.
1. common prefix - present in all words of the list.
1. if we sort the list then we just have to compare the first and last element chars.

> Drawings

<!-- <img src="" alt="img"/> -->

> to code
- sort the list
- compare the chars of first and last elements.