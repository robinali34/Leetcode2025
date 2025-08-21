#!/usr/bin/env python3
"""
Test Configuration for LeetCode Solutions

This file demonstrates how to configure tests to target different solution files.
You can use this to test different implementations, versions, or custom solutions.
"""

import os
from pathlib import Path

# Test configurations for different scenarios
TEST_CONFIGS = {
    "two_sum": {
        "python": {
            "default": "solutions/python/two_sum.py",
            "optimized": "solutions/python/two_sum_optimized.py",  # Example
            "custom": "custom_solutions/two_sum.py"  # Example
        },
        "cpp": {
            "default": {
                "header": "solutions/cpp/two_sum.h",
                "impl": "solutions/cpp/two_sum_impl.cpp"
            },
            "optimized": {
                "header": "solutions/cpp/two_sum_optimized.h",  # Example
                "impl": "solutions/cpp/two_sum_optimized.cpp"   # Example
            }
        }
    }
}

def get_test_config(problem_name: str, language: str, variant: str = "default"):
    """Get test configuration for a specific problem, language, and variant."""
    if problem_name not in TEST_CONFIGS:
        return None
    
    if language not in TEST_CONFIGS[problem_name]:
        return None
    
    config = TEST_CONFIGS[problem_name][language]
    if variant not in config:
        return None
    
    return config[variant]

def run_tests_with_config(problem_name: str, language: str, variant: str = "default"):
    """Run tests using a specific configuration."""
    config = get_test_config(problem_name, language, variant)
    if not config:
        print(f"❌ No configuration found for {problem_name} ({language}, {variant})")
        return False
    
    print(f"🎯 Running tests for {problem_name} ({language}, {variant})")
    print(f"📁 Configuration: {config}")
    
    # Build command for targeted test runner
    if language == "python":
        # For Python, we need to specify the directory containing the solution file
        solution_dir = str(Path(config).parent)
        cmd = [
            "python", "scripts/run_targeted_tests.py",
            problem_name, language,
            "--solution-path", solution_dir
        ]
    else:  # cpp
        cmd = [
            "python", "scripts/run_targeted_tests.py",
            problem_name, language,
            "--header-path", config["header"],
            "--impl-path", config["impl"]
        ]
    
    print(f"🚀 Command: {' '.join(cmd)}")
    
    # Import and run the targeted test runner
    import subprocess
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"💥 Error running tests: {e}")
        return False

def list_available_configs():
    """List all available test configurations."""
    print("📚 Available Test Configurations:")
    print("=" * 50)
    
    for problem_name, languages in TEST_CONFIGS.items():
        print(f"\n🔍 {problem_name.upper()}:")
        for language, variants in languages.items():
            print(f"  {language.upper()}:")
            for variant in variants.keys():
                print(f"    - {variant}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python test_config.py <problem_name> <language> [variant]")
        print("\nExamples:")
        print("  python test_config.py two_sum python")
        print("  python test_config.py two_sum python optimized")
        print("  python test_config.py two_sum cpp default")
        print("  python test_config.py --list")
        print("\nAvailable configurations:")
        list_available_configs()
        sys.exit(1)
    
    if sys.argv[1] == "--list":
        list_available_configs()
        sys.exit(0)
    
    problem_name = sys.argv[1]
    language = sys.argv[2]
    variant = sys.argv[3] if len(sys.argv) > 3 else "default"
    
    success = run_tests_with_config(problem_name, language, variant)
    sys.exit(0 if success else 1) 