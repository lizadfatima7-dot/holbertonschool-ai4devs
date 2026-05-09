# Benchmark Tasks – Copilot Productivity Sprint

## Task 1 - Word Frequency Counter
**Requirements**: Write a Python function that reads a text file and returns the total word count and the top 5 most frequent words with their counts.
**Inputs**: A plain text file path as a string.
**Outputs**: A dictionary containing total_words as an integer and top_5 as a list of tuples with word and count.
**Acceptance Criteria**:
- Returns correct total word count for any valid text file
- Returns exactly 5 most frequent words sorted by count descending
- Ignores punctuation and is case-insensitive
- Raises FileNotFoundError if the file does not exist

---

## Task 2 - REST API Endpoint
**Requirements**: Implement a POST /users endpoint using FastAPI or Express.js with input validation.
**Inputs**: JSON body with name (string, required, min 2 chars) and email (string, required, valid format).
**Outputs**: Created user object with auto-generated ID and timestamp.
**Acceptance Criteria**:
- Returns 201 on successful user creation
- Returns 400 with error message on missing or invalid name
- Returns 400 with error message on invalid or missing email
- Returns 409 if email already exists in the data store
- Response includes id, name, email, and created_at fields

---

## Task 3 - Sorting Algorithm Implementation
**Requirements**: Implement merge sort in Python and include a function to measure and compare its performance against Python's built-in sort on lists of different sizes.
**Inputs**: A list of integers of any size.
**Outputs**: A sorted list of integers in ascending order plus execution time in milliseconds.
**Acceptance Criteria**:
- Returns correctly sorted list for any input including empty list and single element
- Handles duplicate values correctly
- Records execution time in milliseconds for both merge sort and built-in sort
- Prints a comparison table showing input size and time for both methods
- Works correctly for lists with 100, 1000, and 10000 elements

---

## Task 4 - Unit Test Suite
**Requirements**: Write a complete unit test suite for the word frequency counter from Task 1 using pytest.
**Inputs**: Sample text files with known content for testing various scenarios.
**Outputs**: Passing test results with at least 6 test cases covering normal and edge cases.
**Acceptance Criteria**:
- At least 6 test cases covering normal input, empty file, single word, punctuation handling, case insensitivity, and missing file
- All tests pass with pytest
- Tests use fixtures or temporary files rather than hardcoded file paths
- Test coverage report shows at least 90 percent coverage of the target function