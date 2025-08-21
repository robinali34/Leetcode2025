/*
 * Simple test file for Two Sum problem
 * No external dependencies - can be compiled directly
 */

#include <iostream>
#include <vector>
#include <chrono>
#include <cassert>

// Configurable include path - can be overridden via compiler flags
#ifndef SOLUTION_HEADER
#define SOLUTION_HEADER "../solutions/cpp/two_sum.h"
#endif

#ifndef SOLUTION_IMPL
#define SOLUTION_IMPL "../solutions/cpp/two_sum_impl.cpp"
#endif

#include SOLUTION_HEADER
#include SOLUTION_IMPL

class SimpleTest {
private:
    int passed = 0;
    int failed = 0;
    
public:
    void assertEqual(const std::vector<int>& actual, const std::vector<int>& expected, const std::string& testName) {
        if (actual == expected) {
            std::cout << "✅ " << testName << " PASSED" << std::endl;
            passed++;
        } else {
            std::cout << "❌ " << testName << " FAILED" << std::endl;
            std::cout << "   Expected: [";
            for (size_t i = 0; i < expected.size(); i++) {
                if (i > 0) std::cout << ", ";
                std::cout << expected[i];
            }
            std::cout << "]" << std::endl;
            std::cout << "   Actual: [";
            for (size_t i = 0; i < actual.size(); i++) {
                if (i > 0) std::cout << ", ";
                std::cout << actual[i];
            }
            std::cout << "]" << std::endl;
            failed++;
        }
    }
    
    void assertSize(const std::vector<int>& result, size_t expectedSize, const std::string& testName) {
        if (result.size() == expectedSize) {
            std::cout << "✅ " << testName << " PASSED" << std::endl;
            passed++;
        } else {
            std::cout << "❌ " << testName << " FAILED" << std::endl;
            std::cout << "   Expected size: " << expectedSize << std::endl;
            std::cout << "   Actual size: " << result.size() << std::endl;
            failed++;
        }
    }
    
    void assertSum(const std::vector<int>& nums, const std::vector<int>& indices, int target, const std::string& testName) {
        if (indices.size() == 2 && nums[indices[0]] + nums[indices[1]] == target) {
            std::cout << "✅ " << testName << " PASSED" << std::endl;
            passed++;
        } else {
            std::cout << "❌ " << testName << " FAILED" << std::endl;
            if (indices.size() == 2) {
                std::cout << "   Sum: " << nums[indices[0]] << " + " << nums[indices[1]] << " = " 
                         << (nums[indices[0]] + nums[indices[1]]) << " (expected " << target << ")" << std::endl;
            } else {
                std::cout << "   Invalid result size: " << indices.size() << std::endl;
            }
            failed++;
        }
    }
    
    void printSummary() {
        std::cout << "\n" << std::string(50, '=') << std::endl;
        std::cout << "TEST SUMMARY" << std::endl;
        std::cout << std::string(50, '=') << std::endl;
        std::cout << "Passed: " << passed << std::endl;
        std::cout << "Failed: " << failed << std::endl;
        std::cout << "Total: " << (passed + failed) << std::endl;
        
        if (failed == 0) {
            std::cout << "🎉 ALL TESTS PASSED!" << std::endl;
        } else {
            std::cout << "💥 " << failed << " TESTS FAILED!" << std::endl;
        }
        std::cout << std::string(50, '=') << std::endl;
    }
    
    int getFailedCount() const { return failed; }
};

int main() {
    Solution solution;
    SimpleTest test;
    
    std::cout << "🧪 Running Two Sum Tests..." << std::endl;
    std::cout << "📁 Using header: " << SOLUTION_HEADER << std::endl;
    std::cout << "📁 Using implementation: " << SOLUTION_IMPL << std::endl;
    std::cout << std::string(50, '=') << std::endl;
    
    // Test 1: Basic example 1
    {
        std::vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Basic Example 1 - Size");
        test.assertSum(nums, result, target, "Basic Example 1 - Sum");
    }
    
    // Test 2: Basic example 2
    {
        std::vector<int> nums = {3, 2, 4};
        int target = 6;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Basic Example 2 - Size");
        test.assertSum(nums, result, target, "Basic Example 2 - Sum");
    }
    
    // Test 3: Duplicate numbers
    {
        std::vector<int> nums = {3, 3};
        int target = 6;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Duplicate Numbers - Size");
        test.assertSum(nums, result, target, "Duplicate Numbers - Sum");
    }
    
    // Test 4: Negative numbers
    {
        std::vector<int> nums = {-1, -2, -3, -4, -5};
        int target = -8;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Negative Numbers - Size");
        test.assertSum(nums, result, target, "Negative Numbers - Sum");
    }
    
    // Test 5: Large numbers
    {
        std::vector<int> nums = {1000000000, -1000000000, 0, 1, 2};
        int target = 0;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Large Numbers - Size");
        test.assertSum(nums, result, target, "Large Numbers - Sum");
    }
    
    // Test 6: Minimum array size
    {
        std::vector<int> nums = {1, 2};
        int target = 3;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Minimum Array Size - Size");
        test.assertSum(nums, result, target, "Minimum Array Size - Sum");
    }
    
    // Test 7: Large array performance
    {
        const int size = 1000;
        std::vector<int> nums(size);
        for (int i = 0; i < size; i++) {
            nums[i] = i;
        }
        int target = 1997; // 999 + 998 (different indices)
        
        auto start = std::chrono::high_resolution_clock::now();
        std::vector<int> result = solution.twoSum(nums, target);
        auto end = std::chrono::high_resolution_clock::now();
        
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        test.assertSize(result, 2, "Large Array Performance - Size");
        test.assertSum(nums, result, target, "Large Array Performance - Sum");
        std::cout << "   ⏱️  Time: " << duration.count() << " microseconds" << std::endl;
    }
    
    // Test 8: Both solutions match
    {
        std::vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        
        std::vector<int> result1 = solution.twoSum(nums, target);
        std::vector<int> result2 = solution.twoSumBruteForce(nums, target);
        
        test.assertSize(result1, 2, "Both Solutions Match - Result1 Size");
        test.assertSize(result2, 2, "Both Solutions Match - Result2 Size");
        test.assertSum(nums, result1, target, "Both Solutions Match - Result1 Sum");
        test.assertSum(nums, result2, target, "Both Solutions Match - Result2 Sum");
    }
    
    // Test 9: Zero target (with two zeros)
    {
        std::vector<int> nums = {0, 1, 2, 0, 4};
        int target = 0;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "Zero Target - Size");
        test.assertSum(nums, result, target, "Zero Target - Sum");
    }
    
    // Test 10: All same numbers
    {
        std::vector<int> nums = {5, 5, 5, 5, 5};
        int target = 10;
        std::vector<int> result = solution.twoSum(nums, target);
        test.assertSize(result, 2, "All Same Numbers - Size");
        test.assertSum(nums, result, target, "All Same Numbers - Sum");
    }
    
    // Test 11: Performance comparison
    {
        const int size = 1000;
        std::vector<int> nums(size);
        for (int i = 0; i < size; i++) {
            nums[i] = i;
        }
        int target = 1997; // 999 + 998
        
        // Test optimal solution
        auto start = std::chrono::high_resolution_clock::now();
        std::vector<int> result1 = solution.twoSum(nums, target);
        auto end = std::chrono::high_resolution_clock::now();
        auto optimal_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        // Test brute force solution
        start = std::chrono::high_resolution_clock::now();
        std::vector<int> result2 = solution.twoSumBruteForce(nums, target);
        end = std::chrono::high_resolution_clock::now();
        auto brute_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        test.assertSize(result1, 2, "Performance Comparison - Result1 Size");
        test.assertSize(result2, 2, "Performance Comparison - Result2 Size");
        test.assertSum(nums, result1, target, "Performance Comparison - Result1 Sum");
        test.assertSum(nums, result2, target, "Performance Comparison - Result2 Sum");
        
        std::cout << "   ⚡ Performance comparison:" << std::endl;
        std::cout << "     Optimal solution: " << optimal_time.count() << " microseconds" << std::endl;
        std::cout << "     Brute force: " << brute_time.count() << " microseconds" << std::endl;
        std::cout << "     Speedup: " << (double)brute_time.count() / optimal_time.count() << "x" << std::endl;
    }
    
    test.printSummary();
    
    return (test.getFailedCount() == 0) ? 0 : 1;
} 