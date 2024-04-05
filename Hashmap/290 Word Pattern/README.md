# <a href="https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150">290 Word Pattern</a>

### Description

> Tags: *Hash Table, String*

Given a `pattern` and a string `s`, find if `s` follows the same `pattern`.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

 

Example 1:
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```
Example 2:
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```
Example 3:
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```
  
> Understand the problem

1. checkout isomorphic strings (same pattern)
1. we need to map each char to a word in s

> Drawings


> to code

- create a two hashmap to map char to word (pattern -> word) and word to char (word -> pattern)
- check if there is a mismatch and return