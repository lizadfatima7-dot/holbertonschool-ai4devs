$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompt_use_cases.md"
$content = @"
# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and reduce code complexity
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code with explanation of changes

- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions and formatting
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Rewritten code with consistent style and comments

- **Code Review**
  - **Goal**: Identify potential issues before merging
  - **Input**: Pull request diff or function in [LANGUAGE]
  - **Output**: List of issues with severity levels and suggested fixes

## Debugging
- **Error Diagnosis**
  - **Goal**: Identify root cause of a runtime error or unexpected behavior
  - **Input**: Buggy code and stack trace in [LANGUAGE]
  - **Output**: Explanation of root cause and suggested fix

- **Edge Case Detection**
  - **Goal**: Find inputs that cause the function to fail or produce wrong output
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: List of edge cases with expected vs actual behavior

- **Silent Bug Detection**
  - **Goal**: Detect bugs that do not throw errors but produce wrong results
  - **Input**: Function with incorrect output in [LANGUAGE]
  - **Output**: Explanation of logical error and corrected code

## Documentation
- **Docstring Generation**
  - **Goal**: Generate clear and accurate docstrings for undocumented functions
  - **Input**: Function or class definition in [LANGUAGE]
  - **Output**: Docstring following [STYLE] convention such as Google or NumPy

- **README Generation**
  - **Goal**: Create a project README with setup and usage instructions
  - **Input**: Project description and list of main files
  - **Output**: Structured README with installation, usage, and examples sections

- **Inline Comment Generation**
  - **Goal**: Add explanatory comments to complex or unclear code blocks
  - **Input**: Code block in [LANGUAGE]
  - **Output**: Same code with inline comments explaining each step

## Testing
- **Unit Test Generation**
  - **Goal**: Generate unit tests covering normal and edge cases
  - **Input**: Function definition in [LANGUAGE]
  - **Output**: Test file using [FRAMEWORK] with assertions for each case

- **Test Case Design**
  - **Goal**: Design comprehensive test scenarios for a given feature
  - **Input**: Feature description and function signature in [LANGUAGE]
  - **Output**: List of test cases with inputs, expected outputs, and edge cases

- **Mock and Stub Generation**
  - **Goal**: Create mocks for external dependencies in unit tests
  - **Input**: Function that calls external APIs or databases in [LANGUAGE]
  - **Output**: Mock setup code using [FRAMEWORK] with example assertions

## Code Generation
- **Boilerplate Generation**
  - **Goal**: Generate repetitive setup code to save development time
  - **Input**: Project type and technology stack
  - **Output**: Ready-to-use boilerplate with folder structure and config files

- **Algorithm Implementation**
  - **Goal**: Implement a specific algorithm from a description or pseudocode
  - **Input**: Algorithm name or pseudocode in [LANGUAGE]
  - **Output**: Clean implementation with time and space complexity analysis
"@

# Qovluq yoxdursa yarat
$dir = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library"
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir }

[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)