# <a href="https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150">15 3Sum</a>

### Description

> Tags: *Array Two Pointers, Sorting*

Given an integer array `nums`, return all the triplets `[nums[i]`, `nums[j]`, `nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.



Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```
Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```
  
> Understand the problem

1. This problem is basically 2Sum + target = 0
1. we need to find triplets which add up to 0 and unique
1. out of 3 numbers the addition of 2 numbers equal to `0 - third number`

> Drawings

<!-- <img src="" alt="img"/> -->

> to code

- sort the array
- init a `res` array
- loop through the array if the curr and prev element are same skip
- initialise a pointer at curr and another pointer at last element of the array
- while the left pointer is less than right pointer, calc 3Sum -> `curr + left + right`
- if `3Sum < 0` increment left pointer
- elif `3Sum > 0` decrement right pointer
- else append the three pointers `res`, and increment the left pointer also remove the duplicates by comparing the left and left-1 indices