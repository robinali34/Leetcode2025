# Two Sum

**Problem ID:** 1  
**Difficulty:** Easy  
**Category:** Array  
**Tags:** Hash Table, Array

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solution Approach

### Approach 1: Brute Force
- Use two nested loops to check every pair of numbers
- Time Complexity: O(n²)
- Space Complexity: O(1)

### Approach 2: Hash Table (Optimal)
- Use a hash table to store numbers and their indices
- For each number, check if `target - num` exists in the hash table
- Time Complexity: O(n)
- Space Complexity: O(n)

## Implementation

- [C++ Solution](../solutions/cpp/two_sum.cpp)
- [Python Solution](../solutions/python/two_sum.py)

## Test Cases

See the test files for comprehensive test cases covering:
- Basic examples
- Edge cases (duplicate numbers, negative numbers)
- Large arrays
- Various target values 