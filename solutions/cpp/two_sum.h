/*
 * Header file for Two Sum problem
 * Contains only the Solution class definition
 */

#ifndef TWO_SUM_H
#define TWO_SUM_H

#include <vector>

class Solution {
public:
    // Optimal solution using hash table
    std::vector<int> twoSum(std::vector<int>& nums, int target);
    
    // Brute force solution for comparison
    std::vector<int> twoSumBruteForce(std::vector<int>& nums, int target);
};

#endif // TWO_SUM_H 