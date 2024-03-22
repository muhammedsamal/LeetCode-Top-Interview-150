# <a href=""></a>

### Description

> Tags: *String, Two Pointers, String Matching*

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```
Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```
  
> Understand the problem

1. use string slicing to check if the needle is present in haystack

> Drawings

<!-- <img src="" alt="img"/> -->

> to code
- `haystack[i:i+len(needle)] == needle`