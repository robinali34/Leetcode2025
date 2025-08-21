#!/usr/bin/env python3
"""
Script to run all tests for LeetCode solutions.
Supports both C++ and Python solutions.
"""

import os
import sys
import subprocess
import time
from pathlib import Path


def run_python_tests():
    """Run all Python tests using pytest."""
    print("🐍 Running Python tests...")
    print("=" * 50)
    
    try:
        # Find all Python test files
        test_files = list(Path("tests").glob("test_*.py"))
        
        if not test_files:
            print("No Python test files found.")
            return
        
        # Run pytest on each test file
        for test_file in test_files:
            print(f"Testing {test_file.name}...")
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", str(test_file), "-v"],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    print(f"✅ {test_file.name} - PASSED")
                else:
                    print(f"❌ {test_file.name} - FAILED")
                    print(result.stdout)
                    print(result.stderr)
                    
            except subprocess.TimeoutExpired:
                print(f"⏰ {test_file.name} - TIMEOUT")
            except Exception as e:
                print(f"💥 {test_file.name} - ERROR: {e}")
        
        print("=" * 50)
        
    except Exception as e:
        print(f"Error running Python tests: {e}")


def run_cpp_tests():
    """Run all C++ tests using the Makefile."""
    print("⚡ Running C++ tests...")
    print("=" * 50)
    
    try:
        # Check if Makefile exists
        if not Path("Makefile").exists():
            print("Makefile not found. Skipping C++ tests.")
            return
        
        # Check if g++ is available
        try:
            subprocess.run(["g++", "--version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("g++ compiler not found. Skipping C++ tests.")
            return
        
        # Run make test
        print("Compiling and running C++ tests...")
        result = subprocess.run(
            ["make", "test"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            print("✅ All C++ tests passed!")
        else:
            print("❌ Some C++ tests failed.")
            print(result.stdout)
            print(result.stderr)
        
        print("=" * 50)
        
    except subprocess.TimeoutExpired:
        print("⏰ C++ tests timed out.")
    except Exception as e:
        print(f"Error running C++ tests: {e}")


def run_individual_solutions():
    """Run individual solution files directly."""
    print("🚀 Running individual solutions...")
    print("=" * 50)
    
    # Python solutions
    python_solutions = list(Path("solutions/python").glob("*.py"))
    for solution_file in python_solutions:
        print(f"Running {solution_file.name}...")
        try:
            result = subprocess.run(
                [sys.executable, str(solution_file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print(f"✅ {solution_file.name} - SUCCESS")
                # Print first few lines of output
                output_lines = result.stdout.strip().split('\n')
                for line in output_lines[:3]:  # Show first 3 lines
                    if line.strip():
                        print(f"   {line}")
            else:
                print(f"❌ {solution_file.name} - FAILED")
                if result.stderr:
                    print(f"   Error: {result.stderr.strip()}")
                    
        except subprocess.TimeoutExpired:
            print(f"⏰ {solution_file.name} - TIMEOUT")
        except Exception as e:
            print(f"💥 {solution_file.name} - ERROR: {e}")
    
    print("=" * 50)


def check_progress():
    """Check and display current progress."""
    print("📊 Progress Summary")
    print("=" * 50)
    
    try:
        # Count problems by difficulty
        easy_count = len(list(Path("problems/easy").glob("*/")))
        medium_count = len(list(Path("problems/medium").glob("*/")))
        hard_count = len(list(Path("problems/hard").glob("*/")))
        
        # Count solutions
        cpp_count = len(list(Path("solutions/cpp").glob("*.cpp")))
        python_count = len(list(Path("solutions/python").glob("*.py")))
        
        # Count tests
        test_count = len(list(Path("tests").glob("*.py"))) + len(list(Path("tests").glob("*.cpp")))
        
        print(f"📚 Problems:")
        print(f"   Easy: {easy_count}")
        print(f"   Medium: {medium_count}")
        print(f"   Hard: {hard_count}")
        print(f"   Total: {easy_count + medium_count + hard_count}")
        
        print(f"\n💻 Solutions:")
        print(f"   C++: {cpp_count}")
        print(f"   Python: {python_count}")
        
        print(f"\n🧪 Tests: {test_count}")
        
        # Check if progress tracker exists
        if Path("progress/progress_tracker.py").exists():
            print(f"\n📈 Progress tracker available")
            print(f"   Run: python progress/progress_tracker.py")
        
        print("=" * 50)
        
    except Exception as e:
        print(f"Error checking progress: {e}")


def main():
    """Main function to run all tests."""
    print("🧪 LeetCode Test Runner")
    print("=" * 60)
    
    start_time = time.time()
    
    # Check current progress
    check_progress()
    
    # Run tests
    run_python_tests()
    run_cpp_tests()
    
    # Run individual solutions
    run_individual_solutions()
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n⏱️  Total test time: {total_time:.2f} seconds")
    print("🎉 Test run completed!")
    
    print(f"\n💡 Tips:")
    print(f"   - Run individual tests: python -m pytest tests/test_*.py -v")
    print(f"   - Run C++ tests: make test")
    print(f"   - Add new problem: python scripts/add_problem.py")
    print(f"   - Check progress: python progress/progress_tracker.py")


if __name__ == "__main__":
    main() 