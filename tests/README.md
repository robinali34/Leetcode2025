# Testing System for LeetCode Solutions

This directory contains comprehensive test suites for LeetCode solutions in both C++ and Python, with support for targeting specific solution files.

## 🧪 Test Structure

### Python Tests
- **Framework**: pytest
- **Location**: `tests/test_*.py`
- **Features**: 
  - Comprehensive test coverage
  - Parametrized tests
  - Performance testing
  - Edge case validation

### C++ Tests
- **Framework**: Custom test framework (no external dependencies)
- **Location**: `tests/*_simple_test.cpp`
- **Features**:
  - Self-contained tests
  - Performance benchmarking
  - Solution comparison
  - Detailed output formatting

## 🎯 Targeted Testing

The testing system allows you to run tests against specific solution files, making it easy to:
- Test different implementations
- Compare solution versions
- Validate custom solutions
- A/B test algorithms

### Basic Usage

#### 1. Test Specific Problem (Default Solutions)
```bash
# Test Python solution for two_sum
python scripts/run_targeted_tests.py two_sum python

# Test C++ solution for two_sum
python scripts/run_targeted_tests.py two_sum cpp
```

#### 2. Test with Custom Solution Paths
```bash
# Test Python solution from custom location
python scripts/run_targeted_tests.py two_sum python --solution-path /custom/path

# Test C++ solution with custom header and implementation
python scripts/run_targeted_tests.py two_sum cpp \
  --header-path /custom/header.h \
  --impl-path /custom/impl.cpp
```

#### 3. List Available Problems
```bash
python scripts/run_targeted_tests.py --list-problems
```

### Advanced Configuration

#### Using Test Configuration File
```bash
# List available configurations
python tests/test_config.py --list

# Run tests with specific configuration
python tests/test_config.py two_sum python default
python tests/test_config.py two_sum cpp optimized
```

#### Environment Variable Override
```bash
# Override solution path for Python tests
export SOLUTION_PATH=/custom/solutions/python
python -m pytest tests/test_two_sum.py -v
```

## 🔧 Test Configuration

### Python Test Configuration
Python tests can be configured using the `SOLUTION_PATH` environment variable:

```python
# In test files
import os
SOLUTION_PATH = os.getenv('SOLUTION_PATH', os.path.join(os.path.dirname(__file__), '..', 'solutions', 'python'))
sys.path.insert(0, SOLUTION_PATH)
```

### C++ Test Configuration
C++ tests use preprocessor macros for flexible include paths:

```cpp
// In test files
#ifndef SOLUTION_HEADER
#define SOLUTION_HEADER "../solutions/cpp/two_sum.h"
#endif

#ifndef SOLUTION_IMPL
#define SOLUTION_IMPL "../solutions/cpp/two_sum_impl.cpp"
#endif

#include SOLUTION_HEADER
#include SOLUTION_IMPL
```

### Compilation with Custom Paths
```bash
# Compile with custom header and implementation
g++ -std=c++17 -DSOLUTION_HEADER='"custom/header.h"' \
    -DSOLUTION_IMPL='"custom/impl.cpp"' \
    -o test_program test_file.cpp
```

## 📁 File Organization

```
tests/
├── README.md                           # This file
├── test_config.py                      # Test configuration system
├── test_two_sum.py                     # Python tests for two_sum
├── two_sum_simple_test.cpp             # C++ tests for two_sum (no deps)
├── two_sum_test.cpp                    # C++ tests for two_sum (Google Test)
└── [other test files...]
```

## 🚀 Running Tests

### All Tests
```bash
# Run all tests (Python + C++)
python scripts/run_tests.py

# Run only Python tests
python -m pytest tests/ -v

# Run only C++ tests
make test
```

### Individual Tests
```bash
# Run specific Python test
python -m pytest tests/test_two_sum.py -v

# Run specific C++ test
g++ -std=c++17 -o test_program tests/two_sum_simple_test.cpp
./test_program
```

### Targeted Tests
```bash
# Test specific problem and language
python scripts/run_targeted_tests.py two_sum python
python scripts/run_targeted_tests.py two_sum cpp

# Test with custom paths
python scripts/run_targeted_tests.py two_sum python --solution-path /custom/path
```

## 🎨 Creating New Tests

### Python Test Template
```python
import pytest
import sys
import os

# Configurable import path
SOLUTION_PATH = os.getenv('SOLUTION_PATH', os.path.join(os.path.dirname(__file__), '..', 'solutions', 'python'))
sys.path.insert(0, SOLUTION_PATH)

try:
    from problem_name import Solution
except ImportError as e:
    pytest.skip(f"Could not import Solution from {SOLUTION_PATH}: {e}", allow_module_level=True)

class TestProblemName:
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def test_example(self, solution):
        # Your test here
        pass
```

### C++ Test Template
```cpp
#include <iostream>
#include <vector>
#include <cassert>

// Configurable include paths
#ifndef SOLUTION_HEADER
#define SOLUTION_HEADER "../solutions/cpp/problem_name.h"
#endif

#ifndef SOLUTION_IMPL
#define SOLUTION_IMPL "../solutions/cpp/problem_name_impl.cpp"
#endif

#include SOLUTION_HEADER
#include SOLUTION_IMPL

// Your test code here
int main() {
    Solution solution;
    // Test cases...
    return 0;
}
```

## 🔍 Test Discovery

The system automatically discovers:
- **Test files**: Based on naming conventions
- **Solution files**: By scanning solutions directories
- **Problem directories**: From the problems folder structure

### Naming Conventions
- **Python tests**: `test_<problem_name>.py`
- **C++ tests**: `<problem_name>_*.cpp` or `*<problem_name>*.cpp`
- **Solutions**: `<problem_name>.<ext>` in appropriate language directory

## 📊 Test Results

### Python Test Output
```
============================= test session starts =============================
collected 16 items
tests/test_two_sum.py::TestTwoSum::test_basic_example_1 PASSED
tests/test_two_sum.py::TestTwoSum::test_basic_example_2 PASSED
...
16 passed in 1.71s
```

### C++ Test Output
```
🧪 Running Two Sum Tests...
==================================================
✅ Basic Example 1 - Size PASSED
✅ Basic Example 1 - Sum PASSED
...
🎉 ALL TESTS PASSED!
```

## 🛠️ Troubleshooting

### Common Issues

#### Python Import Errors
- Check `SOLUTION_PATH` environment variable
- Verify solution file exists and is importable
- Ensure Python path is correctly set

#### C++ Compilation Errors
- Verify header and implementation files exist
- Check for missing dependencies
- Ensure proper include paths

#### Test Discovery Issues
- Verify test file naming conventions
- Check file permissions
- Ensure test files are in correct directory

### Debug Mode
```bash
# Verbose Python testing
python -m pytest tests/ -v -s

# Verbose C++ compilation
make test VERBOSE=1
```

## 🔄 Continuous Integration

The testing system is designed to work with CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run Python Tests
  run: python -m pytest tests/ -v

- name: Run C++ Tests
  run: make test

- name: Run Targeted Tests
  run: python scripts/run_targeted_tests.py two_sum python
```

## 📈 Performance Testing

Both Python and C++ tests include performance benchmarking:

- **Python**: Uses `time.time()` for execution timing
- **C++**: Uses `std::chrono::high_resolution_clock` for microsecond precision
- **Comparison**: Tests optimal vs. brute force solutions
- **Thresholds**: Configurable performance expectations

## 🎯 Best Practices

1. **Test Coverage**: Include edge cases, boundary conditions, and error scenarios
2. **Performance**: Test with realistic input sizes
3. **Maintainability**: Use descriptive test names and clear assertions
4. **Flexibility**: Design tests to work with different solution implementations
5. **Documentation**: Document test purpose and expected behavior

## 🤝 Contributing

When adding new tests:
1. Follow existing naming conventions
2. Include comprehensive test cases
3. Ensure tests work with the targeted testing system
4. Update this README if adding new features
5. Test both Python and C++ versions when applicable 