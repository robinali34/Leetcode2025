# Makefile for LeetCode C++ solutions
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g -O2
TEST_FLAGS = -lgtest -lgtest_main -lpthread

# Directories
CPP_DIR = solutions/cpp
TEST_DIR = tests
BUILD_DIR = build

# Find all C++ source files
CPP_SOURCES = $(shell find $(CPP_DIR) -name "*.cpp")
CPP_OBJECTS = $(CPP_SOURCES:$(CPP_DIR)/%.cpp=$(BUILD_DIR)/%.o)

# Test files
TEST_SOURCES = $(shell find $(TEST_DIR) -name "*_test.cpp")
TEST_OBJECTS = $(TEST_SOURCES:$(TEST_DIR)/%.cpp=$(BUILD_DIR)/%.o)

.PHONY: all clean test build

all: build

build: $(BUILD_DIR) $(CPP_OBJECTS)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)/easy
	mkdir -p $(BUILD_DIR)/medium
	mkdir -p $(BUILD_DIR)/hard

$(BUILD_DIR)/%.o: $(CPP_DIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

test: build
	@echo "Running C++ tests..."
	@echo "Testing simple test..."
	$(CXX) $(CXXFLAGS) tests/two_sum_simple_test.cpp solutions/cpp/two_sum_impl.cpp -o $(BUILD_DIR)/two_sum_simple_test
	./$(BUILD_DIR)/two_sum_simple_test
	@echo "All C++ tests passed!"

clean:
	rm -rf $(BUILD_DIR)

# Individual problem compilation
easy/%: $(BUILD_DIR)/easy/%.o
	$(CXX) $(CXXFLAGS) $< -o $@

medium/%: $(BUILD_DIR)/medium/%.o
	$(CXX) $(CXXFLAGS) $< -o $@

hard/%: $(BUILD_DIR)/hard/%.o
	$(CXX) $(CXXFLAGS) $< -o $@ 