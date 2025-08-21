/*
 * LeetCode Problem: Two Sum
 * Difficulty: Easy
 * Problem ID: 1
 * 
 * Problem Description:
 * Given an array of integers nums and an integer target, return indices of the two numbers
 * such that they add up to target. You may assume that each input would have exactly one
 * solution, and you may not use the same element twice.
 * 
 * Example:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * 
 * Constraints:
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * Only one valid answer exists.
 * 
 * Solution Approach:
 * Use hash table to store numbers and their indices. For each number, check if
 * target - num exists in the hash table.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;

class Solution {
public:
    // Optimal solution using hash table
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            
            numMap[nums[i]] = i;
        }
        
        return {}; // No solution found
    }
    
    // Brute force solution for comparison
    vector<int> twoSumBruteForce(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {}; // No solution found
    }
};

// Test function
void testSolution() {
    Solution sol;
    
    // Test case 1: Basic example
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = sol.twoSum(nums1, target1);
    assert(result1.size() == 2);
    assert(nums1[result1[0]] + nums1[result1[1]] == target1);
    cout << "Test case 1 passed: [2,7,11,15], target=9 -> [" 
         << result1[0] << "," << result1[1] << "]" << endl;
    
    // Test case 2: Another example
    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> result2 = sol.twoSum(nums2, target2);
    assert(result2.size() == 2);
    assert(nums2[result2[0]] + nums2[result2[1]] == target2);
    cout << "Test case 2 passed: [3,2,4], target=6 -> [" 
         << result2[0] << "," << result2[1] << "]" << endl;
    
    // Test case 3: Duplicate numbers
    vector<int> nums3 = {3, 3};
    int target3 = 6;
    vector<int> result3 = sol.twoSum(nums3, target3);
    assert(result3.size() == 2);
    assert(nums3[result3[0]] + nums3[result3[1]] == target3);
    cout << "Test case 3 passed: [3,3], target=6 -> [" 
         << result3[0] << "," << result3[1] << "]" << endl;
    
    // Test case 4: Negative numbers
    vector<int> nums4 = {-1, -2, -3, -4, -5};
    int target4 = -8;
    vector<int> result4 = sol.twoSum(nums4, target4);
    assert(result4.size() == 2);
    assert(nums4[result4[0]] + nums4[result4[1]] == target4);
    cout << "Test case 4 passed: [-1,-2,-3,-4,-5], target=-8 -> [" 
         << result4[0] << "," << result4[1] << "]" << endl;
    
    // Test case 5: Large array
    vector<int> nums5(1000);
    for (int i = 0; i < 1000; i++) {
        nums5[i] = i;
    }
    int target5 = 1998; // 999 + 999
    vector<int> result5 = sol.twoSum(nums5, target5);
    assert(result5.size() == 2);
    assert(nums5[result5[0]] + nums5[result5[1]] == target5);
    cout << "Test case 5 passed: Large array test" << endl;
    
    // Test both solutions give same results
    vector<int> result1_brute = sol.twoSumBruteForce(nums1, target1);
    assert(result1 == result1_brute);
    cout << "Brute force and optimal solutions match" << endl;
    
    cout << "All test cases passed!" << endl;
}

int main() {
    testSolution();
    return 0;
} 