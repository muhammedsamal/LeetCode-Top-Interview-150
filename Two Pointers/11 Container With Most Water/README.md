# <a href="https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150">11 Container With Most Water</a>

### Description

> Tags: *Array, Two Pointers, Greedy*

You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

![container](assets/image-C.png)

Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:
```
Input: height = [1,1]
Output: 1
```
  
> Understand the problem

1. container with most water -> maximum aread = max(length * breadth)
1. height = min(l1, l2)
1. breadth = l1 - l2 + 1

> Drawings

![alt text](assets/image.png)
![alt text](assets/image-1.png)
![alt text](assets/image-2.png)

> to code

- two pointers at start and end of the array
- height = min(two pointers)
- breadth = l2 - l1 + 1
- max(area)
