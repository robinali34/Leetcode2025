/*
 * Test file for Two Sum problem
 * Uses Google Test framework
 */

#include <gtest/gtest.h>
#include <vector>
#include <chrono>
#include "../solutions/cpp/two_sum.cpp"

class TwoSumTest : public ::testing::Test {
protected:
    Solution solution;
    
    void SetUp() override {
        // Set up any common test data
    }
    
    void TearDown() override {
        // Clean up after tests
    }
};

// Basic functionality tests
TEST_F(TwoSumTest, BasicExample1) {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, BasicExample2) {
    std::vector<int> nums = {3, 2, 4};
    int target = 6;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, DuplicateNumbers) {
    std::vector<int> nums = {3, 3};
    int target = 6;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

// Edge cases
TEST_F(TwoSumTest, NegativeNumbers) {
    std::vector<int> nums = {-1, -2, -3, -4, -5};
    int target = -8;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, LargeNumbers) {
    std::vector<int> nums = {1000000000, -1000000000, 0, 1, 2};
    int target = 0;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, MinimumArraySize) {
    std::vector<int> nums = {1, 2};
    int target = 3;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

// Performance tests
TEST_F(TwoSumTest, LargeArrayPerformance) {
    const int size = 10000;
    std::vector<int> nums(size);
    for (int i = 0; i < size; i++) {
        nums[i] = i;
    }
    int target = 19997; // 9999 + 9998 (different indices)
    
    auto start = std::chrono::high_resolution_clock::now();
    std::vector<int> result = solution.twoSum(nums, target);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
    EXPECT_LT(duration.count(), 10000); // Should complete in less than 10ms
}

// Comparison tests
TEST_F(TwoSumTest, BothSolutionsMatch) {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    std::vector<int> result1 = solution.twoSum(nums, target);
    std::vector<int> result2 = solution.twoSumBruteForce(nums, target);
    
    ASSERT_EQ(result1.size(), 2);
    ASSERT_EQ(result2.size(), 2);
    
    // Both should sum to target
    EXPECT_EQ(nums[result1[0]] + nums[result1[1]], target);
    EXPECT_EQ(nums[result2[0]] + nums[result2[1]], target);
    
    // Both should be valid solutions (order might differ)
    bool valid_solution = false;
    if ((result1[0] == result2[0] && result1[1] == result2[1]) ||
        (result1[0] == result2[1] && result1[1] == result2[0])) {
        valid_solution = true;
    }
    EXPECT_TRUE(valid_solution);
}

// Additional edge cases
TEST_F(TwoSumTest, ZeroTarget) {
    std::vector<int> nums = {0, 1, 2, 3, 4};
    int target = 0;
    std::vector<int> result = solution.twoSum(nums, target);
    
    // Should find 0 + 0 = 0
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, SingleElementArray) {
    std::vector<int> nums = {1};
    int target = 2;
    std::vector<int> result = solution.twoSum(nums, target);
    
    // Should return empty vector for single element
    EXPECT_EQ(result.size(), 0);
}

TEST_F(TwoSumTest, EmptyArray) {
    std::vector<int> nums = {};
    int target = 5;
    std::vector<int> result = solution.twoSum(nums, target);
    
    // Should return empty vector for empty array
    EXPECT_EQ(result.size(), 0);
}

TEST_F(TwoSumTest, AllSameNumbers) {
    std::vector<int> nums = {5, 5, 5, 5, 5};
    int target = 10;
    std::vector<int> result = solution.twoSum(nums, target);
    
    // Should find two 5s that sum to 10
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

TEST_F(TwoSumTest, LargeNegativeTarget) {
    std::vector<int> nums = {-1000000, -999999, 0, 1, 2};
    int target = -1999999;
    std::vector<int> result = solution.twoSum(nums, target);
    
    ASSERT_EQ(result.size(), 2);
    EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
}

// Stress tests
TEST_F(TwoSumTest, StressTest) {
    const int num_tests = 50;  // Reduced for faster testing
    const int array_size = 1000;
    
    for (int test = 0; test < num_tests; test++) {
        std::vector<int> nums(array_size);
        for (int i = 0; i < array_size; i++) {
            nums[i] = i;
        }
        
        // Test various targets
        for (int target = 0; target < 100; target += 10) {
            std::vector<int> result = solution.twoSum(nums, target);
            
            if (target < array_size * 2 - 1) {
                // Should find a solution
                ASSERT_EQ(result.size(), 2);
                EXPECT_EQ(nums[result[0]] + nums[result[1]], target);
            }
        }
    }
}

// Performance comparison test
TEST_F(TwoSumTest, PerformanceComparison) {
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
    
    // Both should find valid solutions
    ASSERT_EQ(result1.size(), 2);
    ASSERT_EQ(result2.size(), 2);
    EXPECT_EQ(nums[result1[0]] + nums[result1[1]], target);
    EXPECT_EQ(nums[result2[0]] + nums[result2[1]], target);
    
    // Optimal solution should be faster
    EXPECT_LT(optimal_time.count(), brute_time.count());
    
    std::cout << "Performance comparison:" << std::endl;
    std::cout << "  Optimal solution: " << optimal_time.count() << " microseconds" << std::endl;
    std::cout << "  Brute force: " << brute_time.count() << " microseconds" << std::endl;
    std::cout << "  Speedup: " << (double)brute_time.count() / optimal_time.count() << "x" << std::endl;
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
} 