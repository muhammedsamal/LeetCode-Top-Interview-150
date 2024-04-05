# <a href="https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150">205 Isomorphic Strings</a>

### Description

> Tags: *Hash Table, String*

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:
```
Input: s = "egg", t = "add"
Output: true
```
Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```
Example 3:
```
Input: s = "paper", t = "title"
Output: true
```

> Understand the problem

1. all occurence of char must be replaced with another char while perserving the order of chars.
1. no tow chars may map to the same char
1. a char may map to itself
1. chars frequency matters, also the mapping matters
1. if the frequency count is same then -> isomorphic
1. order of chars matters

> Drawings


> to code

- built two hashmap of char frequency of both `s` and `t` strings
- check if there is a mismatch in frequncy count of char in both hashmap
- add the chars to hashmap as `s -> t` and `t -> s`