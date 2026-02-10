# fun-100-extended - Python Fundamentals & Problem Solving (Extended)

# Learning Outcomes assessed:

- Understanding of Basic python syntax
- Conditional statements
- Functions
- Basic loops
- List manipulation
- String manipulation
- Simple algorithms (Problem solving)

---

# Assessment Structure

This is a coding-only assessment with 7 Python programming challenges.

## Scoring & Weighting

Your coding score is determined by the number of tests you pass.

Let:
- T = total number of coding tests
- P = number of tests you pass

```bash
Coding Score = (P / T) × 100%
```

### Pass Mark

To pass the overall assessment, your score must be **60% (Minimum Pass Mark) or higher**.

---

## How to run your tests

To run all your tests:

```bash
python3 -m pytest test_fundamentals.py -v
```

To run your tests individually:

```bash
python3 -m pytest test_fundamentals.py::TestExtendedFunctions::test_fizzbuzz_output -v
```

---

# Extended Fundamentals Coding Assessment

This assessment consists of seven Python functions. Each function tests your understanding of loops, conditionals, string manipulation, and list operations.

## Project Structure

```
first_step/
├── fundamentals.py          # <-- This is where you write your solutions
├── test_fundamentals.py     # <-- These are the tests you must make pass
└── README.md                # <-- Assessment instructions (this file) 
```

---

## Question 1 - `fizzbuzz(n)`

**User Story:**
*As a developer, I want to print the classic FizzBuzz sequence from 1 to n, so that I can demonstrate my understanding of conditionals and loops.*

**Requirements:**
- Print numbers from 1 to n (inclusive)
- For multiples of 3, print "Fizz" instead of the number
- For multiples of 5, print "Buzz" instead of the number
- For multiples of both 3 and 5, print "FizzBuzz"
- Each output should be on a new line

**Example:**
```python
fizzbuzz(15)
# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
```

---

## Question 2 - `count_vowels(text)`

**User Story:**
*As a text analyst, I want to count the number of vowels in a given string, so that I can analyze text patterns.*

**Requirements:**
- Count all vowels (a, e, i, o, u) in the input string
- Count should be case-insensitive (both 'A' and 'a' count as vowels)
- Return the total count as an integer
- Return 0 for empty strings or strings with no vowels

**Example:**
```python
count_vowels("hello")      # Returns: 2
count_vowels("AEIOU")      # Returns: 5
count_vowels("rhythm")     # Returns: 0
```

---

## Question 3 - `is_palindrome(text)`

**User Story:**
*As a word game enthusiast, I want to check if a word or phrase is a palindrome, so that I can validate palindromic entries.*

**Requirements:**
- Check if the text reads the same forwards and backwards
- Ignore spaces and capitalization
- Return True if it's a palindrome, False otherwise
- Empty strings are considered palindromes

**Example:**
```python
is_palindrome("racecar")                        # Returns: True
is_palindrome("A man a plan a canal Panama")    # Returns: True
is_palindrome("hello")                          # Returns: False
```

---

## Question 4 - `find_max(numbers)`

**User Story:**
*As a data analyst, I want to find the maximum value in a list of numbers without using the built-in max() function, so that I can understand iteration logic.*

**Requirements:**
- Find and return the largest number in the list
- Do NOT use Python's built-in `max()` function
- Return None if the list is empty
- Handle negative numbers correctly

**Example:**
```python
find_max([1, 5, 3, 9, 2])     # Returns: 9
find_max([-5, -2, -10, -1])   # Returns: -1
find_max([])                  # Returns: None
```

---

## Question 5 - `calculate_average(numbers)`

**User Story:**
*As a teacher, I want to calculate the average of student grades, so that I can determine class performance.*

**Requirements:**
- Calculate and return the average of all numbers in the list
- Return the result as a float
- Return 0 for an empty list
- Handle both positive and negative numbers

**Example:**
```python
calculate_average([10, 20, 30])      # Returns: 20.0
calculate_average([1, 2, 3, 4, 5])   # Returns: 3.0
calculate_average([])                # Returns: 0
```

---

## Question 6 - `remove_duplicates(numbers)`

**User Story:**
*As a data cleaner, I want to remove duplicate values from a list while preserving the original order, so that I can work with unique values only.*

**Requirements:**
- Remove all duplicate numbers from the list
- Preserve the order of first occurrence
- Return a new list with unique values only
- Do NOT use set() directly (as it doesn't preserve order)

**Example:**
```python
remove_duplicates([1, 2, 2, 3, 4, 4, 5])    # Returns: [1, 2, 3, 4, 5]
remove_duplicates([1, 1, 1, 1])              # Returns: [1]
remove_duplicates([])                        # Returns: []
```

---

## Question 7 - `multiplication_table(n)`

**User Story:**
*As a math student, I want to see the multiplication table for any number from 1 to 10, so that I can practice my multiplication skills.*

**Requirements:**
- Print the multiplication table for number n
- Show multiplications from 1 × n to 10 × n
- Format: "1 x n = result" (each on a new line)
- Use the exact format shown in the example

**Example:**
```python
multiplication_table(3)
# Output:
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# 4 x 3 = 12
# 5 x 3 = 15
# 6 x 3 = 18
# 7 x 3 = 21
# 8 x 3 = 24
# 9 x 3 = 27
# 10 x 3 = 30
```

---

# Your Goal

Create all functions in `fundamentals.py` so that:
- The code is valid Python
- Each function behaves according to the requirements above
- All unit tests pass successfully

## Tips for Success

1. **Read the user story and requirements carefully** - understand what each function should do
2. **Test incrementally** - run tests for one function at a time
3. **Pay attention to edge cases** - empty lists, empty strings, negative numbers
4. **Use appropriate data types** - strings, integers, floats, lists, booleans
5. **Follow the exact output format** - especially for print statements

Good luck! 🚀