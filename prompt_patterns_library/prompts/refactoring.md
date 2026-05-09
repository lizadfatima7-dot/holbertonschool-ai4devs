$base = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts"
if (-not (Test-Path $base)) { New-Item -ItemType Directory -Path $base }

# refactoring.md
[System.IO.File]::WriteAllText("$base\refactoring.md", @"
# Refactoring Prompt Template

**Role**: Senior Developer
**Task**: Refactor the given [LANGUAGE] code for clarity, readability, and performance.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Clean, optimized code with inline comments explaining each change made.
"@, [System.Text.Encoding]::ASCII)

# style_enforcement.md
[System.IO.File]::WriteAllText("$base\style_enforcement.md", @"
# Style Enforcement Prompt Template

**Role**: Code Quality Reviewer
**Task**: Rewrite the given [LANGUAGE] code block to enforce consistent naming conventions and formatting rules.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Rewritten code with snake_case variables, consistent indentation, and a comment above each logical block.
"@, [System.Text.Encoding]::ASCII)

# code_review.md
[System.IO.File]::WriteAllText("$base\code_review.md", @"
# Code Review Prompt Template

**Role**: Senior Developer performing a pre-merge code review
**Task**: Review the given [LANGUAGE] code and identify all potential issues including bugs, security risks, and style violations.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Numbered list of issues with severity level (High, Medium, Low) and a suggested fix for each issue.
"@, [System.Text.Encoding]::ASCII)

# error_diagnosis.md
[System.IO.File]::WriteAllText("$base\error_diagnosis.md", @"
# Error Diagnosis Prompt Template

**Role**: Debugging Expert
**Task**: Analyze the given [LANGUAGE] code and stack trace to identify the root cause of the error and suggest a fix.
**Input Placeholder**: [CODE_BLOCK] and [STACK_TRACE]
**Expected Output**: Root cause explanation in plain language, corrected code with comments highlighting what was changed and why.
"@, [System.Text.Encoding]::ASCII)

# edge_case_detection.md
[System.IO.File]::WriteAllText("$base\edge_case_detection.md", @"
# Edge Case Detection Prompt Template

**Role**: QA Engineer
**Task**: Analyze the given [LANGUAGE] function and identify all edge cases that could cause it to fail or return incorrect results.
**Input Placeholder**: [FUNCTION_DEFINITION]
**Expected Output**: List of edge cases with input value, expected output, actual output, and a suggested fix for each failing case.
"@, [System.Text.Encoding]::ASCII)

# silent_bug_detection.md
[System.IO.File]::WriteAllText("$base\silent_bug_detection.md", @"
# Silent Bug Detection Prompt Template

**Role**: Senior Developer specializing in logical errors
**Task**: Analyze the given [LANGUAGE] function that produces incorrect results without throwing errors and identify the logical bug.
**Input Placeholder**: [CODE_BLOCK] and [INCORRECT_OUTPUT_EXAMPLE]
**Expected Output**: Explanation of the logical error, before and after code comparison, and corrected implementation with comments.
"@, [System.Text.Encoding]::ASCII)

# docstring_generation.md
[System.IO.File]::WriteAllText("$base\docstring_generation.md", @"
# Docstring Generation Prompt Template

**Role**: Technical Writer with software development expertise
**Task**: Generate a complete docstring for the given [LANGUAGE] function following the [STYLE] convention.
**Input Placeholder**: [FUNCTION_DEFINITION]
**Expected Output**: Docstring covering function purpose, all parameters with types and descriptions, return value with type, and any exceptions that may be raised.
"@, [System.Text.Encoding]::ASCII)

# readme_generation.md
[System.IO.File]::WriteAllText("$base\readme_generation.md", @"
# README Generation Prompt Template

**Role**: Technical Writer and Developer Advocate
**Task**: Create a structured README file for the given project based on the description and list of main files provided.
**Input Placeholder**: [PROJECT_DESCRIPTION] and [FILE_LIST]
**Expected Output**: README with sections for Project Overview, Requirements, Installation steps, Usage examples with code snippets, Configuration options table, and Contributing guidelines.
"@, [System.Text.Encoding]::ASCII)

# unit_test_generation.md
[System.IO.File]::WriteAllText("$base\unit_test_generation.md", @"
# Unit Test Generation Prompt Template

**Role**: QA Engineer with expertise in test-driven development
**Task**: Generate a complete unit test file for the given [LANGUAGE] function using the [FRAMEWORK] testing framework.
**Input Placeholder**: [FUNCTION_DEFINITION]
**Expected Output**: Test file with one test function per case covering normal inputs, boundary values, and edge cases, each with clear assertions and descriptive test names.
"@, [System.Text.Encoding]::ASCII)

# test_case_design.md
[System.IO.File]::WriteAllText("$base\test_case_design.md", @"
# Test Case Design Prompt Template

**Role**: QA Engineer designing a comprehensive test plan
**Task**: Design a full set of test cases for the given [LANGUAGE] feature based on the description and function signature.
**Input Placeholder**: [FEATURE_DESCRIPTION] and [FUNCTION_SIGNATURE]
**Expected Output**: Structured list of test cases each containing input values, expected output, actual output placeholder, and notes on edge cases or special conditions.
"@, [System.Text.Encoding]::ASCII)

# mock_generation.md
[System.IO.File]::WriteAllText("$base\mock_generation.md", @"
# Mock and Stub Generation Prompt Template

**Role**: Backend Developer writing isolated unit tests
**Task**: Generate mock and stub code for the external dependencies in the given [LANGUAGE] function using the [FRAMEWORK] mocking library.
**Input Placeholder**: [FUNCTION_WITH_DEPENDENCIES]
**Expected Output**: Complete mock setup code with patched dependencies, example test function using the mocks, and assertions verifying the function behaves correctly without real external calls.
"@, [System.Text.Encoding]::ASCII)

# boilerplate_generation.md
[System.IO.File]::WriteAllText("$base\boilerplate_generation.md", @"
# Boilerplate Generation Prompt Template

**Role**: Senior Developer initializing a new project
**Task**: Generate complete boilerplate code for a [PROJECT_TYPE] project using the [TECH_STACK] technology stack.
**Input Placeholder**: [PROJECT_TYPE] and [TECH_STACK]
**Expected Output**: Ready-to-use project structure with folder layout, main entry file, configuration files, dependency list, and setup instructions.
"@, [System.Text.Encoding]::ASCII)

# algorithm_implementation.md
[System.IO.File]::WriteAllText("$base\algorithm_implementation.md", @"
# Algorithm Implementation Prompt Template

**Role**: Software Engineer implementing data structures and algorithms
**Task**: Implement the given algorithm or data structure in [LANGUAGE] based on the provided description or pseudocode.
**Input Placeholder**: [ALGORITHM_DESCRIPTION] or [PSEUDOCODE]
**Expected Output**: Clean implementation with time complexity analysis, space complexity analysis, and a usage example demonstrating the algorithm on a sample input.
"@, [System.Text.Encoding]::ASCII)

# api_integration.md
[System.IO.File]::WriteAllText("$base\api_integration.md", @"
# API Integration Scaffold Prompt Template

**Role**: Backend Developer integrating third party services
**Task**: Generate scaffold code for integrating the [API_NAME] API in [LANGUAGE] based on the provided endpoint description.
**Input Placeholder**: [API_NAME], [ENDPOINT_DESCRIPTION], and [AUTH_METHOD]
**Expected Output**: Scaffold code including authentication setup, HTTP request handling, JSON response parsing, error handling for network failures, and a typed return value.
"@, [System.Text.Encoding]::ASCII)

# inline_comments.md
[System.IO.File]::WriteAllText("$base\inline_comments.md", @"
# Inline Comment Generation Prompt Template

**Role**: Senior Developer improving code maintainability
**Task**: Add clear and concise inline comments to the given [LANGUAGE] code block to explain the purpose and logic of each step.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Same code with an inline comment above or beside each logical step explaining what it does and why it is necessary.
"@, [System.Text.Encoding]::ASCII)

Write-Host "Done - 15 files created"