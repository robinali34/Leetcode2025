"""
Test file for Two Sum problem
Uses pytest framework
"""

import pytest
import sys
import os
import time

# Configurable import path - can be overridden via environment variable or command line
SOLUTION_PATH = os.getenv('SOLUTION_PATH', os.path.join(os.path.dirname(__file__), '..', 'solutions', 'python'))

# Add the solutions directory to the path
sys.path.insert(0, SOLUTION_PATH)

try:
    from two_sum import Solution
except ImportError as e:
    pytest.skip(f"Could not import Solution from {SOLUTION_PATH}: {e}", allow_module_level=True)


class TestTwoSum:
    """Test class for Two Sum solution."""
    
    @pytest.fixture
    def solution(self):
        """Create a solution instance for each test."""
        return Solution()
    
    def test_basic_example_1(self, solution):
        """Test basic example: [2,7,11,15], target=9."""
        nums = [2, 7, 11, 15]
        target = 9
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print(f"Test case 1 passed: [2,7,11,15], target=9 -> {result}")
    
    def test_basic_example_2(self, solution):
        """Test example: [3,2,4], target=6."""
        nums = [3, 2, 4]
        target = 6
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print(f"Test case 2 passed: [3,2,4], target=6 -> {result}")
    
    def test_duplicate_numbers(self, solution):
        """Test duplicate numbers: [3,3], target=6."""
        nums = [3, 3]
        target = 6
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print(f"Test case 3 passed: [3,3], target=6 -> {result}")
    
    def test_negative_numbers(self, solution):
        """Test negative numbers: [-1,-2,-3,-4,-5], target=-8."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print(f"Test case 4 passed: [-1,-2,-3,-4,-5], target=-8 -> {result}")
    
    def test_large_numbers(self, solution):
        """Test large numbers."""
        nums = [1000000000, -1000000000, 0, 1, 2]
        target = 0
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print("Test case 5 passed: Large numbers test")
    
    def test_minimum_array_size(self, solution):
        """Test minimum array size: [1,2], target=3."""
        nums = [1, 2]
        target = 3
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        print("Test case 6 passed: Minimum array size test")
    
    def test_large_array_performance(self, solution):
        """Test large array performance."""
        size = 1000
        nums = list(range(size))
        target = 1997  # 999 + 998 (different indices)
        
        start_time = time.time()
        result = solution.twoSum(nums, target)
        end_time = time.time()
        
        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
        assert duration < 100  # Should complete in less than 100ms
        print(f"Test case 7 passed: Large array performance test ({duration:.2f}ms)")
    
    def test_solutions_match(self, solution):
        """Test that both solutions give the same results."""
        nums = [2, 7, 11, 15]
        target = 9
        
        result1 = solution.twoSum(nums, target)
        result2 = solution.twoSumBruteForce(nums, target)
        
        # Both should find valid solutions
        assert len(result1) == 2
        assert len(result2) == 2
        
        # Both should sum to target
        assert nums[result1[0]] + nums[result1[1]] == target
        assert nums[result2[0]] + nums[result2[1]] == target
        
        print("Test case 8 passed: Both solutions match")
    
    def test_no_solution(self, solution):
        """Test case where no solution exists."""
        nums = [1, 2, 3, 4]
        target = 10  # No two numbers sum to 10
        
        result = solution.twoSum(nums, target)
        assert result == []
        print("Test case 9 passed: No solution case")
    
    def test_stress_test(self, solution):
        """Stress test with multiple test cases."""
        num_tests = 50
        array_size = 1000
        
        for test in range(num_tests):
            nums = list(range(array_size))
            
            # Test various targets that are guaranteed to have solutions
            for target in range(1, 100, 10):
                result = solution.twoSum(nums, target)
                
                if target < array_size * 2 - 1:
                    # Should find a solution
                    assert len(result) == 2
                    assert nums[result[0]] + nums[result[1]] == target
        
        print("Test case 10 passed: Stress test")
    
    @pytest.mark.parametrize("nums,target,expected_sum", [
        ([2, 7, 11, 15], 9, 9),
        ([3, 2, 4], 6, 6),
        ([3, 3], 6, 6),
        ([0, 4, 3, 0], 0, 0),
        ([-3, 4, 3, 90], 0, 0),
    ])
    def test_parametrized_cases(self, solution, nums, target, expected_sum):
        """Test multiple cases using pytest parametrize."""
        result = solution.twoSum(nums, target)
        
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == expected_sum
        print(f"Parametrized test passed: {nums}, target={target} -> {result}")


def test_performance_comparison():
    """Test performance comparison between both solutions."""
    solution = Solution()
    
    # Create a large test case
    nums = list(range(1000))
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
    # Run pytest with verbose output
    pytest.main([__file__, "-v"]) 