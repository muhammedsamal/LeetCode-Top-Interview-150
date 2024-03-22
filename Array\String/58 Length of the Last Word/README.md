# <a href="https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150">58 Length of the Last Word</a>

### Description

> Tags: *String*

Given a string s consisting of words and spaces, return the length of the ***last*** word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```
Example 2:
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```
Example 3:
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```
  
> Understand the problem

1. strings consist of words and spaces
1. return the last word length without spaces

> Drawings

<!-- <img src="" alt="img"/> -->

> to code
- use .split() to convert the list of words
- return the length of the last element of the list