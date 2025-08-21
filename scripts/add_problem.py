#!/usr/bin/env python3
"""
Utility script to add new LeetCode problems to the project.
This script creates the necessary directory structure and template files.
"""

import os
import sys
from pathlib import Path
from typing import Optional


def create_problem_structure(problem_id: str, title: str, difficulty: str, 
                           category: str = "Array", tags: Optional[list] = None):
    """
    Create the complete structure for a new LeetCode problem.
    
    Args:
        problem_id: LeetCode problem ID
        title: Problem title
        difficulty: Easy, Medium, or Hard
        category: Problem category (default: Array)
        tags: List of problem tags
    """
    # Normalize inputs
    difficulty = difficulty.lower()
    title_slug = title.lower().replace(" ", "_").replace("-", "_")
    
    if tags is None:
        tags = []
    
    # Create directories
    problem_dir = Path(f"problems/{difficulty}/{title_slug}")
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create README.md
    readme_content = f"""# {title}

**Problem ID:** {problem_id}  
**Difficulty:** {difficulty.capitalize()}  
**Category:** {category}  
**Tags:** {", ".join(tags)}

## Problem Description

[DESCRIBE THE PROBLEM HERE]

## Examples

**Example 1:**
```
Input: [PROVIDE INPUT]
Output: [PROVIDE OUTPUT]
Explanation: [EXPLAIN THE EXAMPLE]
```

## Constraints

[LIST CONSTRAINTS]

## Solution Approach

### Approach 1: [APPROACH NAME]
- [DESCRIBE APPROACH]
- Time Complexity: O([COMPLEXITY])
- Space Complexity: O([COMPLEXITY])

## Implementation

- [C++ Solution](../../../solutions/cpp/{title_slug}.cpp)
- [Python Solution](../../../solutions/python/{title_slug}.py)

## Test Cases

See the test files for comprehensive test cases covering:
- Basic examples
- Edge cases
- Large inputs
- Various scenarios
"""
    
    with open(problem_dir / "README.md", "w") as f:
        f.write(readme_content)
    
    # Create C++ solution file
    cpp_content = f"""/*
 * LeetCode Problem: {title}
 * Difficulty: {difficulty.capitalize()}
 * Problem ID: {problem_id}
 * 
 * Problem Description:
 * [DESCRIBE THE PROBLEM HERE]
 * 
 * Example:
 * [PROVIDE EXAMPLES]
 * 
 * Constraints:
 * [LIST CONSTRAINTS]
 * 
 * Solution Approach:
 * [EXPLAIN YOUR APPROACH]
 * 
 * Time Complexity: O([COMPLEXITY])
 * Space Complexity: O([COMPLEXITY])
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>

using namespace std;

class Solution {{
public:
    // TODO: Implement your solution here
    // Example: vector<int> solve(vector<int>& nums) {{ ... }}
    
    // Helper functions can be added here
}};

// Test function
void testSolution() {{
    Solution sol;
    
    // TODO: Add your test cases here
    
    cout << "All test cases passed!" << endl;
}}

int main() {{
    testSolution();
    return 0;
}}
"""
    
    cpp_file = Path(f"solutions/cpp/{title_slug}.cpp")
    cpp_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cpp_file, "w") as f:
        f.write(cpp_content)
    
    # Create Python solution file
    python_content = f'''"""
LeetCode Problem: {title}
Difficulty: {difficulty.capitalize()}
Problem ID: {problem_id}

Problem Description:
[DESCRIBE THE PROBLEM HERE]

Example:
[PROVIDE EXAMPLES]

Constraints:
[LIST CONSTRAINTS]

Solution Approach:
[EXPLAIN YOUR APPROACH]

Time Complexity: O([COMPLEXITY])
Space Complexity: O([COMPLEXITY])
"""

from typing import List, Optional, Dict, Set, Tuple
import unittest


class Solution:
    """Solution class for the {title} problem."""
    
    def solve(self, nums: List[int]) -> int:
        """
        Main solution function.
        
        Args:
            nums: Input array
            
        Returns:
            Solution result
        """
        # TODO: Implement your solution here
        pass
    
    def helper_function(self, data):
        """Helper function if needed."""
        pass


class TestSolution(unittest.TestCase):
    """Test cases for the solution."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test example 1."""
        # TODO: Add your test cases here
        # Example: self.assertEqual(self.solution.solve([1, 2, 3]), expected_result)
        pass
    
    def test_example_2(self):
        """Test example 2."""
        # TODO: Add your test cases here
        pass
    
    def test_edge_cases(self):
        """Test edge cases."""
        # TODO: Add edge case tests
        pass


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
    
    # Or run solution directly
    # solution = Solution()
    # result = solution.solve([1, 2, 3])
    # print(f"Result: {{result}}")
'''
    
    python_file = Path(f"solutions/python/{title_slug}.py")
    python_file.parent.mkdir(parents=True, exist_ok=True)
    with open(python_file, "w") as f:
        f.write(python_content)
    
    # Create C++ test file
    cpp_test_content = f"""/*
 * Test file for {title} problem
 * Uses Google Test framework
 */

#include <gtest/gtest.h>
#include <vector>
#include <chrono>
#include "../solutions/cpp/{title_slug}.cpp"

class {title.replace(" ", "")}Test : public ::testing::Test {{
protected:
    Solution solution;
    
    void SetUp() override {{
        // Set up any common test data
    }}
    
    void TearDown() override {{
        // Clean up after tests
    }}
}};

// TODO: Add your test cases here
TEST_F({title.replace(" ", "")}Test, BasicExample) {{
    // TODO: Implement test case
}}

int main(int argc, char **argv) {{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}}
"""
    
    cpp_test_file = Path(f"tests/{title_slug}_test.cpp")
    cpp_test_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cpp_test_file, "w") as f:
        f.write(cpp_test_content)
    
    # Create Python test file
    python_test_content = f'''"""
Test file for {title} problem
Uses pytest framework
"""

import pytest
import sys
import os

# Add the solutions directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions', 'python'))

from {title_slug} import Solution


class Test{title.replace(" ", "")}:
    """Test class for {title} solution."""
    
    @pytest.fixture
    def solution(self):
        """Create a solution instance for each test."""
        return Solution()
    
    def test_example_1(self, solution):
        """Test example 1."""
        # TODO: Add your test cases here
        pass
    
    def test_example_2(self, solution):
        """Test example 2."""
        # TODO: Add your test cases here
        pass
    
    def test_edge_cases(self, solution):
        """Test edge cases."""
        # TODO: Add edge case tests
        pass


if __name__ == "__main__":
    # Run pytest with verbose output
    pytest.main([__file__, "-v"])
'''
    
    python_test_file = Path(f"tests/test_{title_slug}.py")
    python_test_file.parent.mkdir(parents=True, exist_ok=True)
    with open(python_test_file, "w") as f:
        f.write(python_test_content)
    
    print(f"✅ Created problem structure for '{title}' (ID: {problem_id})")
    print(f"📁 Problem directory: {problem_dir}")
    print(f"📝 C++ solution: {cpp_file}")
    print(f"🐍 Python solution: {python_file}")
    print(f"🧪 C++ tests: {cpp_test_file}")
    print(f"🧪 Python tests: {python_test_file}")
    print(f"📚 README: {problem_dir}/README.md")
    print("\nNext steps:")
    print("1. Fill in the problem description in the README")
    print("2. Implement your solution in both C++ and Python")
    print("3. Add comprehensive test cases")
    print("4. Update the progress tracker")


def main():
    """Main function to run the script interactively."""
    print("🚀 LeetCode Problem Setup Script")
    print("=" * 40)
    
    # Get problem details
    problem_id = input("Enter LeetCode Problem ID: ").strip()
    title = input("Enter Problem Title: ").strip()
    
    # Get difficulty
    while True:
        difficulty = input("Enter Difficulty (Easy/Medium/Hard): ").strip().lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        print("Please enter Easy, Medium, or Hard")
    
    # Get category
    category = input("Enter Category (default: Array): ").strip()
    if not category:
        category = "Array"
    
    # Get tags
    tags_input = input("Enter tags (comma-separated, default: none): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
    
    # Confirm
    print(f"\n📋 Problem Details:")
    print(f"ID: {problem_id}")
    print(f"Title: {title}")
    print(f"Difficulty: {difficulty.capitalize()}")
    print(f"Category: {category}")
    print(f"Tags: {', '.join(tags) if tags else 'None'}")
    
    confirm = input("\nProceed with creation? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        create_problem_structure(problem_id, title, difficulty, category, tags)
    else:
        print("❌ Cancelled")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line usage
        if len(sys.argv) >= 4:
            problem_id = sys.argv[1]
            title = sys.argv[2]
            difficulty = sys.argv[3]
            category = sys.argv[4] if len(sys.argv) > 4 else "Array"
            tags = sys.argv[5].split(",") if len(sys.argv) > 5 else []
            
            create_problem_structure(problem_id, title, difficulty, category, tags)
        else:
            print("Usage: python add_problem.py <problem_id> <title> <difficulty> [category] [tags]")
            print("Example: python add_problem.py 1 'Two Sum' easy Array 'Hash Table,Array'")
    else:
        # Interactive mode
        main() 