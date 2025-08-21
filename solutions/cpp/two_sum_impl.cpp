/*
 * Implementation file for Two Sum problem
 * Contains only the Solution class implementation
 */

#include "two_sum.h"
#include <unordered_map>
#include <cstddef>

std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> numMap;
    
    for (size_t i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], static_cast<int>(i)};
        }
        
        numMap[nums[i]] = static_cast<int>(i);
    }
    
    return {}; // No solution found
}

std::vector<int> Solution::twoSumBruteForce(std::vector<int>& nums, int target) {
    for (size_t i = 0; i < nums.size(); i++) {
        for (size_t j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                return {static_cast<int>(i), static_cast<int>(j)};
            }
        }
    }
    return {}; // No solution found
} 