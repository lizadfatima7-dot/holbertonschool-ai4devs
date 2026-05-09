$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompt_use_cases.md"
$content = @"
# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and reduce code complexity
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code with explanation of each change made
  - **Example Output**: Refactored function with descriptive variable names, extracted helper functions, and a summary of complexity improvements

- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions and formatting rules
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Rewritten code with consistent style and inline comments
  - **Example Output**: Same logic rewritten with snake_case variables, 4-space indentation, and a comment above each logical block

- **Code Review**
  - **Goal**: Identify potential issues and improvements before merging
  - **Input**: Function or diff in [LANGUAGE]
  - **Output**: Numbered list of issues with severity and suggested fix for each
  - **Example Output**: 1. High - Missing null check on line 5. Suggested fix: add if input is None return early. 2. Low - Variable name x is not descriptive. Rename to user_count.

## Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime error or unexpected behavior
  - **Input**: Buggy code and stack trace in [LANGUAGE]
  - **Output**: Root cause explanation and corrected code with comments
  - **Example Output**: Root cause: index out of bounds because loop uses len+1. Fix: change range(0, len+1) to range(0, len).

- **Edge Case Detection**
  - **Goal**: Find inputs that cause the function to fail or return wrong results
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: List of edge cases with expected output and actual output for each
  - **Example Output**: Edge case: empty list. Expected: return 0. Actual: raises ZeroDivisionError. Edge case: n greater than list length. Expected: return full list. Actual: IndexError.

- **Silent Bug Detection**
  - **Goal**: Detect bugs that produce wrong results without throwing errors
  - **Input**: Function with incorrect output in [LANGUAGE]
  - **Output**: Explanation of logical error and corrected code with before and after comparison
  - **Example Output**: Before: result = 0. After: result = 1. Explanation: multiplicative accumulator must start at 1 not 0.

## Documentation

- **Docstring Generation**
  - **Goal**: Generate accurate docstrings for undocumented functions
  - **Input**: Function or class definition in [LANGUAGE]
  - **Output**: Docstring in [STYLE] format covering parameters, return values, and exceptions
  - **Example Output**: Args: items (list) - input list. n (int) - number of elements. Returns: list - last n elements. Raises: IndexError if n exceeds list length.

- **README Generation**
  - **Goal**: Create a structured project README with setup and usage instructions
  - **Input**: Project description and list of main files
  - **Output**: README with installation steps, usage examples, and configuration options
  - **Example Output**: Sections: Project Overview, Requirements, Installation with pip install commands, Usage with code snippet, Configuration table, and Contributing guidelines.

- **Inline Comment Generation**
  - **Goal**: Add explanatory comments to complex or unclear code blocks
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Same code with inline comments explaining the purpose of each step
  - **Example Output**: Each line or logical block annotated with a comment explaining what it does and why it is needed.

## Testing

- **Unit Test Generation**
  - **Goal**: Generate unit tests covering normal cases and edge cases
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: Test file using [FRAMEWORK] with one test function per case and clear assertions
  - **Example Output**: test_normal_case asserts get_last_n([1,2,3,4,5], 3) equals [3,4,5]. test_edge_empty asserts get_last_n([], 0) equals [].

- **Test Case Design**
  - **Goal**: Design comprehensive test scenarios for a given feature
  - **Input**: Feature description and function signature in [LANGUAGE]
  - **Output**: Structured list of test cases with input values, expected output, and edge case notes
  - **Example Output**: Case 1: normal input [1,2,3] n=2 expects [2,3]. Case 2: n=0 expects []. Case 3: n equals list length expects full list. Case 4: empty list expects [].

- **Mock and Stub Generation**
  - **Goal**: Create mocks for external dependencies to enable isolated unit testing
  - **Input**: Function that calls external APIs or databases in [LANGUAGE]
  - **Output**: Mock setup code using [FRAMEWORK] with example test assertions
  - **Example Output**: Mock fetch returning fake user array. Assert getUserNames returns uppercased names without making real HTTP request.

## Code Generation

- **Boilerplate Generation**
  - **Goal**: Generate repetitive setup code to accelerate project initialization
  - **Input**: Project type and technology stack description
  - **Output**: Ready-to-use boilerplate with folder structure, config files, and setup instructions
  - **Example Output**: Flask project with app.py, requirements.txt, config.py, and folder structure including routes, models, and templates directories.

- **Algorithm Implementation**
  - **Goal**: Implement a specific algorithm from a description or pseudocode
  - **Input**: Algorithm name or pseudocode and target language [LANGUAGE]
  - **Output**: Clean implementation with time complexity, space complexity, and usage example
  - **Example Output**: Binary search function with O(log n) time complexity, O(1) space complexity, and example call showing search in sorted list.

- **API Integration Scaffold**
  - **Goal**: Generate starter code for integrating a third party API
  - **Input**: API name, endpoint description, and target language [LANGUAGE]
  - **Output**: Scaffold code with authentication, request handling, and error handling included
  - **Example Output**: Function calling REST API with Bearer token header, try-except for network errors, and JSON response parsing with typed return value.
"@
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)