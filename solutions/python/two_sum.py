"""
LeetCode Problem: Two Sum
Difficulty: Easy
Problem ID: 1

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Solution Approach:
Use hash table to store numbers and their indices. For each number, check if
target - num exists in the hash table.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import unittest


class Solution:
    """Solution class for the Two Sum problem."""
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal solution using hash table.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices whose values sum to target
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
        
        return []  # No solution found
    
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force solution for comparison.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices whose values sum to target
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # No solution found


class TestSolution(unittest.TestCase):
    """Test cases for the Two Sum solution."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test basic example: [2,7,11,15], target=9."""
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
        print(f"Test case 1 passed: [2,7,11,15], target=9 -> {result}")
    
    def test_example_2(self):
        """Test example: [3,2,4], target=6."""
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
        print(f"Test case 2 passed: [3,2,4], target=6 -> {result}")
    
    def test_example_3(self):
        """Test duplicate numbers: [3,3], target=6."""
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
        print(f"Test case 3 passed: [3,3], target=6 -> {result}")
    
    def test_negative_numbers(self):
        """Test negative numbers: [-1,-2,-3,-4,-5], target=-8."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
        print(f"Test case 4 passed: [-1,-2,-3,-4,-5], target=-8 -> {result}")
    
    def test_large_array(self):
        """Test large array performance."""
        nums = list(range(1000))
        target = 1997  # 999 + 998 (different indices)
        result = self.solution.twoSum(nums, target)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)
        print("Test case 5 passed: Large array test")
    
    def test_solutions_match(self):
        """Test that both solutions give the same results."""
        nums = [2, 7, 11, 15]
        target = 9
        
        result1 = self.solution.twoSum(nums, target)
        result2 = self.solution.twoSumBruteForce(nums, target)
        
        # Both should find valid solutions
        self.assertEqual(len(result1), 2)
        self.assertEqual(len(result2), 2)
        
        # Both should sum to target
        self.assertEqual(nums[result1[0]] + nums[result1[1]], target)
        self.assertEqual(nums[result2[0]] + nums[result2[1]], target)
        
        print("Brute force and optimal solutions match")
    
    def test_no_solution(self):
        """Test case where no solution exists."""
        nums = [1, 2, 3, 4]
        target = 10  # No two numbers sum to 10
        
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [])
        print("Test case 6 passed: No solution case")


def run_performance_comparison():
    """Compare performance of both solutions."""
    import time
    
    solution = Solution()
    
    # Create a large test case
    nums = list(range(1000))  # Reduced size for faster testing
    target = 1997  # 999 + 998 (different indices)
    
    # Test optimal solution
    start_time = time.time()
    result1 = solution.twoSum(nums, target)
    optimal_time = time.time() - start_time
    
    # Test brute force solution
    start_time = time.time()
    result2 = solution.twoSumBruteForce(nums, target)
    brute_time = time.time() - start_time
    
    print(f"\nPerformance Comparison:")
    print(f"Optimal solution time: {optimal_time:.6f} seconds")
    print(f"Brute force solution time: {brute_time:.6f} seconds")
    print(f"Speedup: {brute_time/optimal_time:.2f}x")
    
    # Verify both give same result
    assert result1 == result2
    print("Both solutions give identical results")


if __name__ == "__main__":
    # Run tests
    print("Running unit tests...")
    unittest.main(verbosity=2, exit=False)
    
    # Run performance comparison
    print("\n" + "="*50)
    run_performance_comparison()
    
    # Example usage
    print("\n" + "="*50)
    print("Example usage:")
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {target}") 