$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompt_use_cases.md"
$content = @"
# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and reduce code complexity
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code with explanation of each change made

- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions and formatting rules
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Rewritten code with consistent style and inline comments

- **Code Review**
  - **Goal**: Identify potential issues and improvements before merging
  - **Input**: Function or diff in [LANGUAGE]
  - **Output**: Numbered list of issues with severity and suggested fix for each

## Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime error or unexpected behavior
  - **Input**: Buggy code and stack trace in [LANGUAGE]
  - **Output**: Root cause explanation and corrected code with comments

- **Edge Case Detection**
  - **Goal**: Find inputs that cause the function to fail or return wrong results
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: List of edge cases with expected output and actual output for each

- **Silent Bug Detection**
  - **Goal**: Detect bugs that produce wrong results without throwing errors
  - **Input**: Function with incorrect output in [LANGUAGE]
  - **Output**: Explanation of logical error and corrected code with before and after comparison

## Documentation

- **Docstring Generation**
  - **Goal**: Generate accurate docstrings for undocumented functions
  - **Input**: Function or class definition in [LANGUAGE]
  - **Output**: Docstring in [STYLE] format covering parameters, return values, and exceptions

- **README Generation**
  - **Goal**: Create a structured project README with setup and usage instructions
  - **Input**: Project description and list of main files
  - **Output**: README with installation steps, usage examples, and configuration options

- **Inline Comment Generation**
  - **Goal**: Add explanatory comments to complex or unclear code blocks
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Same code with inline comments explaining the purpose of each step

## Testing

- **Unit Test Generation**
  - **Goal**: Generate unit tests covering normal cases and edge cases
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: Test file using [FRAMEWORK] with one test function per case and clear assertions

- **Test Case Design**
  - **Goal**: Design comprehensive test scenarios for a given feature
  - **Input**: Feature description and function signature in [LANGUAGE]
  - **Output**: Structured list of test cases with input values, expected output, and edge case notes

- **Mock and Stub Generation**
  - **Goal**: Create mocks for external dependencies to enable isolated unit testing
  - **Input**: Function that calls external APIs or databases in [LANGUAGE]
  - **Output**: Mock setup code using [FRAMEWORK] with example test assertions

## Code Generation

- **Boilerplate Generation**
  - **Goal**: Generate repetitive setup code to accelerate project initialization
  - **Input**: Project type and technology stack description
  - **Output**: Ready-to-use boilerplate with folder structure, config files, and setup instructions

- **Algorithm Implementation**
  - **Goal**: Implement a specific algorithm from a description or pseudocode
  - **Input**: Algorithm name or pseudocode and target language [LANGUAGE]
  - **Output**: Clean implementation with time complexity, space complexity, and usage example

- **API Integration Scaffold**
  - **Goal**: Generate starter code for integrating a third party API
  - **Input**: API name, endpoint description, and target language [LANGUAGE]
  - **Output**: Scaffold code with authentication, request handling, and error handling included
"@
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)