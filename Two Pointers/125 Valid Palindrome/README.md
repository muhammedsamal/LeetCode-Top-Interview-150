# <a href="https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150">125 Valid Palindrome</a>

### Description

> Tags: *Two Pointers, String*

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

 

Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

> Understand the problem

1. remove all non-alphanumeric chars
1. all uppercase to lowercase
1. use another string for comparison to reversed string

> Drawings

<!-- <img src="" alt="img"/> -->

> to code
- initialise an empty string to store the non-alphanumeric char
- return `str = res[::-1]`