# LeetCode Training Tracker 2025 🚀

A comprehensive project to track your LeetCode training progress with solutions in both C++ and Python, along with comprehensive test cases and progress monitoring.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![C++](https://img.shields.io/badge/C++-17+-red.svg)](https://isocpp.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](https://github.com/robinali34/Leetcode2025)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Features

- **Multi-language Support**: Solutions in both C++ and Python
- **Comprehensive Testing**: Extensive test suites with pytest and custom C++ framework
- **Progress Tracking**: Monitor completion status, difficulty levels, and performance metrics
- **Targeted Testing**: Test specific solution files or custom implementations
- **Templates**: Ready-to-use solution templates for new problems
- **Organization**: Problems organized by difficulty level
- **Documentation**: Detailed problem descriptions and solution explanations
- **Performance Analysis**: Compare different solution approaches

## 🏗️ Project Structure

```
LC2025/
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── Makefile                 # C++ compilation and testing
├── requirements.txt         # Python dependencies
├── problems/                # LeetCode problems organized by difficulty
│   ├── easy/
│   │   ├── two_sum/        # Problem documentation
│   │   └── valid_parentheses/
│   ├── medium/
│   └── hard/
├── solutions/               # Solutions in C++ and Python
│   ├── cpp/
│   │   ├── two_sum.h       # Header files
│   │   ├── two_sum_impl.cpp # Implementation files
│   │   └── two_sum.cpp     # Original solution files
│   └── python/
│       └── two_sum.py      # Python solutions
├── tests/                   # Comprehensive test suites
│   ├── README.md           # Testing documentation
│   ├── test_two_sum.py     # Python tests (pytest)
│   ├── two_sum_simple_test.cpp # C++ tests (no deps)
│   └── two_sum_test.cpp    # C++ tests (Google Test)
├── progress/                # Progress tracking files
│   ├── progress_tracker.py  # Main progress tracker
│   ├── problems.json       # Progress data
│   └── leetcode_progress.csv # Progress export
├── templates/               # Solution templates
│   ├── cpp_solution_template.cpp
│   └── python_solution_template.py
└── scripts/                 # Utility scripts
    ├── add_problem.py       # Add new problems
    ├── run_tests.py         # Run all tests
    └── run_targeted_tests.py # Target specific solutions
```

## 🚀 Quick Start

### Prerequisites

- **C++ compiler** (g++ recommended, C++17+)
- **Python 3.8+**
- **Make** (optional, for C++ compilation)
- **Git** (for version control)

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:robinali34/Leetcode2025.git
   cd Leetcode2025
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   # Test Python setup
   python -m pytest --version
   
   # Test C++ setup
   g++ --version
   ```

## 🧪 Testing System

### Running Tests

#### **All Tests**
```bash
# Run complete test suite (Python + C++)
python scripts/run_tests.py

# Run only Python tests
python -m pytest tests/ -v

# Run only C++ tests
make test
```

#### **Targeted Testing**
```bash
# Test specific problem and language
python scripts/run_targeted_tests.py two_sum python
python scripts/run_targeted_tests.py two_sum cpp

# Test with custom solution paths
python scripts/run_targeted_tests.py two_sum python --solution-path /custom/path
python scripts/run_targeted_tests.py two_sum cpp --header-path /custom/header.h --impl-path /custom/impl.cpp

# List available problems
python scripts/run_targeted_tests.py --list-problems
```

#### **Individual Tests**
```bash
# Python tests
python -m pytest tests/test_two_sum.py -v

# C++ tests
g++ -std=c++17 -o test_program tests/two_sum_simple_test.cpp
./test_program
```

### Test Features

- **Python Tests**: pytest framework with comprehensive coverage
- **C++ Tests**: Custom framework (no external dependencies)
- **Performance Testing**: Benchmarking and comparison
- **Edge Case Coverage**: Boundary conditions and error scenarios
- **Flexible Paths**: Test any solution file from any location

## 📝 Adding New LeetCode Solutions

### **Automated Setup (Recommended)**

Use the built-in script to create complete problem structure:

```bash
# Interactive mode
python scripts/add_problem.py

# Command line mode
python scripts/add_problem.py <problem_id> <title> <difficulty> [category] [tags]

# Example
python scripts/add_problem.py 5 "Longest Palindromic Substring" medium "String" "Dynamic Programming,String"
```

This creates:
- Problem documentation in `problems/[difficulty]/[problem_name]/`
- C++ solution template in `solutions/cpp/`
- Python solution template in `solutions/python/`
- Test files in `tests/`
- Proper directory structure

### **Manual Setup**

1. **Create problem directory**
   ```bash
   mkdir -p problems/easy/problem_name
   ```

2. **Add problem documentation**
   ```bash
   # Create README.md with problem description
   # Include examples, constraints, and solution approach
   ```

3. **Implement solutions**
   ```bash
   # C++: Create header (.h) and implementation (.cpp) files
   # Python: Create solution file (.py)
   ```

4. **Add test cases**
   ```bash
   # Python: Add to existing test file or create new one
   # C++: Add to existing test file or create new one
   ```

### **Solution Templates**

#### **C++ Template**
```cpp
/*
 * LeetCode Problem: [PROBLEM_NAME]
 * Difficulty: [EASY/MEDIUM/HARD]
 * Problem ID: [PROBLEM_ID]
 */

#include <iostream>
#include <vector>
#include <string>
// ... other includes

class Solution {
public:
    // TODO: Implement your solution here
    // Example: vector<int> solve(vector<int>& nums) { ... }
};

int main() {
    Solution sol;
    // TODO: Add test cases
    return 0;
}
```

#### **Python Template**
```python
"""
LeetCode Problem: [PROBLEM_NAME]
Difficulty: [EASY/MEDIUM/HARD]
Problem ID: [PROBLEM_ID]
"""

from typing import List, Optional
import unittest

class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass

class TestSolution(unittest.TestCase):
    def test_example(self):
        # TODO: Add test cases
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

## 📊 Progress Tracking

### **Track Your Progress**
```bash
# View current progress
python progress/progress_tracker.py

# Add new problem to tracking
python -c "
from progress.progress_tracker import ProgressTracker
tracker = ProgressTracker()
tracker.add_problem('5', 'Longest Palindromic Substring', 'Medium', 'String')
"

# Mark problem as completed
python -c "
from progress.progress_tracker import ProgressTracker
tracker = ProgressTracker()
tracker.mark_completed('5', 'python', 30, 'Used dynamic programming approach')
"
```

### **Progress Features**
- **Completion tracking** by problem and language
- **Difficulty analysis** and performance metrics
- **Time tracking** for each solution
- **Rating system** for problem difficulty
- **Export to CSV** for external analysis
- **JSON storage** for programmatic access

## 🔧 Configuration

### **Environment Variables**
```bash
# Override Python solution path
export SOLUTION_PATH=/custom/solutions/python

# Run tests with custom path
python -m pytest tests/test_two_sum.py -v
```

### **C++ Compilation Flags**
```bash
# Custom header and implementation paths
g++ -std=c++17 \
    -DSOLUTION_HEADER='"custom/header.h"' \
    -DSOLUTION_IMPL='"custom/impl.cpp"' \
    -o test_program test_file.cpp
```

### **Test Configuration**
```bash
# Use configuration system
python tests/test_config.py --list
python tests/test_config.py two_sum python default
python tests/test_config.py two_sum cpp optimized
```

## 📈 Performance Testing

### **Built-in Benchmarks**
- **Python**: `time.time()` for execution timing
- **C++**: `std::chrono::high_resolution_clock` for microsecond precision
- **Comparison**: Optimal vs. brute force solutions
- **Thresholds**: Configurable performance expectations

### **Performance Analysis**
```bash
# Run performance comparison
python solutions/python/two_sum.py

# C++ performance test
./tests/two_sum_simple_test
```

## 🛠️ Development

### **Adding New Features**
1. **Create feature branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Implement changes**
   ```bash
   # Make your changes
   # Add tests for new functionality
   ```

3. **Test thoroughly**
   ```bash
   python scripts/run_tests.py
   make test
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add new feature: description"
   git push origin feature/new-feature
   ```

### **Code Quality**
- **Python**: Follow PEP 8 style guide
- **C++**: Use consistent formatting and naming conventions
- **Tests**: Maintain high test coverage
- **Documentation**: Keep README files updated

## 🔍 Troubleshooting

### **Common Issues**

#### **Python Import Errors**
```bash
# Check solution path
echo $SOLUTION_PATH

# Verify file exists
ls -la solutions/python/

# Test import manually
python -c "import sys; sys.path.insert(0, 'solutions/python'); from two_sum import Solution"
```

#### **C++ Compilation Errors**
```bash
# Check compiler version
g++ --version

# Verify file existence
ls -la solutions/cpp/

# Test compilation manually
g++ -std=c++17 -o test solutions/cpp/two_sum_impl.cpp
```

#### **Test Discovery Issues**
```bash
# Check file permissions
ls -la tests/

# Verify naming conventions
find tests/ -name "*two_sum*"

# Run with verbose output
python -m pytest tests/ -v -s
```

### **Debug Mode**
```bash
# Verbose Python testing
python -m pytest tests/ -v -s

# Verbose C++ compilation
make test VERBOSE=1

# Check git status
git status
git remote -v
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests for new functionality**
5. **Ensure all tests pass**
6. **Submit a pull request**

### **Contribution Guidelines**
- Follow existing code style and conventions
- Add comprehensive test coverage
- Update documentation as needed
- Test both Python and C++ versions when applicable
- Include performance analysis for new solutions

## 📚 Resources

### **LeetCode Resources**
- [LeetCode Official Site](https://leetcode.com/)
- [LeetCode Problems](https://leetcode.com/problemset/all/)
- [LeetCode Discuss](https://leetcode.com/discuss/)

### **Testing Resources**
- [pytest Documentation](https://docs.pytest.org/)
- [Google Test Framework](https://google.github.io/googletest/)
- [C++ Testing Best Practices](https://github.com/google/googletest)

### **Learning Resources**
- [C++ Reference](https://en.cppreference.com/)
- [Python Documentation](https://docs.python.org/)
- [Data Structures & Algorithms](https://github.com/trekhleb/javascript-algorithms)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LeetCode** for providing excellent algorithmic problems
- **Open source community** for testing frameworks and tools
- **Contributors** who help improve this project

## 📞 Support

If you encounter any issues or have questions:

1. **Check the troubleshooting section** above
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed information
4. **Join discussions** in the project's GitHub Discussions

---

**Happy coding and happy LeetCode solving! 🎉**

*Remember: The best way to learn algorithms is to practice, test, and iterate. This project helps you do all three effectively.* 