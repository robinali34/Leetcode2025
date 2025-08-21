# LeetCode Training Tracker

A comprehensive project to track your LeetCode training progress with solutions in both C++ and Python, along with test cases and progress monitoring.

## Project Structure

```
LC2025/
├── README.md                 # This file
├── problems/                 # LeetCode problems organized by difficulty
│   ├── easy/
│   ├── medium/
│   └── hard/
├── solutions/                # Solutions in C++ and Python
│   ├── cpp/
│   └── python/
├── tests/                    # Test cases for each problem
├── progress/                 # Progress tracking files
├── templates/                # Solution templates
├── scripts/                  # Utility scripts
└── requirements.txt          # Python dependencies
```

## Features

- **Multi-language Support**: Solutions in both C++ and Python
- **Test Cases**: Comprehensive test cases for each problem
- **Progress Tracking**: Monitor your completion status and performance
- **Templates**: Ready-to-use solution templates
- **Organization**: Problems organized by difficulty level
- **Documentation**: Detailed problem descriptions and solution explanations

## Getting Started

### Prerequisites

- C++ compiler (g++ recommended)
- Python 3.8+
- Make (optional, for C++ compilation)

### Setup

1. Clone or download this project
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have a C++ compiler installed

### Usage

1. **Adding a new problem**:
   - Create a new directory in `problems/[difficulty]/[problem_name]`
   - Add your solution files in `solutions/cpp/` and `solutions/python/`
   - Create test cases in `tests/`

2. **Running tests**:
   ```bash
   # Python tests
   python -m pytest tests/
   
   # C++ tests (using the provided Makefile)
   make test
   ```

3. **Tracking progress**:
   - Update the progress files in the `progress/` directory
   - Use the provided scripts to generate progress reports

## Problem Template

Each problem should include:
- Problem description
- Solution approach
- Time and space complexity analysis
- Test cases
- C++ and Python implementations

## Contributing

Feel free to add new problems, improve existing solutions, or enhance the testing framework.

## License

This project is for educational purposes. Use it to improve your algorithmic problem-solving skills! 