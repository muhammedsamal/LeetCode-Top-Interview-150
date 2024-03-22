# <a href="">151 Reverse the Words in a String</a>

### Description

> Tags: *String, Two Pointers*

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```
Example 2:
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```
Example 3:
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

> Understand the problem

1. reverse the order of words. 
1. `s` may contain leading or trailing spaces or multiple spaces between two words.
1. returned string should only have a single space separating the words.

> Drawings

<!-- <img src="" alt="img"/> -->

> to code
- use `.split()` to convert the string into a list.
- use `[::-1]` to reverse a word in the list
- use `" ".join()` to concatinate the words of the list into a single string