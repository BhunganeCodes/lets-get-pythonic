# loopy-300 - Python Loops & Iteration Mastery (New Edition)

# Learning Outcomes assessed:

- Advanced loop techniques
- List comprehension and iteration
- String manipulation with loops
- User input validation with loops
- Pattern matching with regular expressions
- Dictionary manipulation
- Mathematical operations in loops
- Complex algorithmic thinking

---

# Assessment Structure

This is a coding-only assessment with 7 Python programming challenges focused on loops and iteration.

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
python3 -m pytest test_loopy_new.py -v
```

To run your tests individually:

```bash
python3 -m pytest test_loopy_new.py::TestFunctions::test_recipe_scaler_multiple_ingredients -v
```

---

# Loopy Coding Assessment - New Edition

This assessment consists of seven Python functions that test your mastery of loops, iteration patterns, and algorithmic problem-solving.

## Project Structure

```
loopy-new-assessment/
├── loopy_new.py              # <-- This is where you write your solutions
├── test_loopy_new.py         # <-- These are the tests you must make pass
└── README.md                 # <-- Assessment instructions (this file) 
```

---

## Question 1 - `recipe_scaler(ingredients, multiplier)`

**User Story:**
*As a professional chef running a catering business, I need to scale recipe ingredient quantities up or down based on the number of guests, so I can prepare the exact amounts needed without waste or shortages.*

**Requirements:**
- Accept a list of ingredient quantities (integers or floats)
- Accept a multiplier (can be any positive number: 2 for double, 0.5 for half, etc.)
- Return a new list with all quantities multiplied by the multiplier
- Return an empty list if input is empty
- Results can be integers or floats

**Example:**
```python
recipe_scaler([50, 100, 25], 3)      # Returns: [150, 300, 75]
recipe_scaler([200, 100, 50], 0.5)   # Returns: [100, 50, 25]
recipe_scaler([10, 20, 30], 1)       # Returns: [10, 20, 30]
recipe_scaler([], 2)                 # Returns: []
```

**Implementation Notes:**
- Loop through ingredients and multiply each by the multiplier
- Simple list comprehension works well
- Handle both integers and floats

---

## Question 2 - `temperature_converter(celsius_temps)`

**User Story:**
*As a travel blogger writing about my international adventures, I need to convert Celsius temperatures to Fahrenheit for my American audience, so they can better understand the weather conditions I experienced.*

**Requirements:**
- Accept a list of temperatures in Celsius
- Convert each temperature to Fahrenheit using: `F = (C × 9/5) + 32`
- Return a list of Fahrenheit temperatures as integers (rounded)
- Return an empty list if input is empty
- Handle negative temperatures

**Example:**
```python
temperature_converter([0, 100, -40])    # Returns: [32, 212, -40]
temperature_converter([20, 25, 30])     # Returns: [68, 77, 86]
temperature_converter([])               # Returns: []
```

**Implementation Notes:**
- Formula: `(celsius * 9/5) + 32`
- Convert results to integers
- Use list comprehension or loop

---

## Question 3 - `password_strength()`

**User Story:**
*As a security-conscious application developer, I need to enforce strong password creation by rejecting weak passwords and prompting users repeatedly until they create a password that meets minimum security standards.*

**Requirements:**
- Continuously prompt user with "Enter a password:" until a strong password is entered
- A strong password must contain:
  - At least 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character from: `!@#$%^&*`
- Print "Too weak. Try again." for weak passwords
- Print "Strong password accepted!" for strong passwords
- Use `input()` to get user input

**Example:**
```python
password_strength()
# User enters: weak
# Output: Too weak. Try again.
# User enters: StrongP@ss123
# Output: Strong password accepted!
```

**Implementation Notes:**
- Use a `while True` loop
- Check each requirement separately
- Use string methods like `isupper()`, `islower()`, `isdigit()`
- Check for special characters with `in` operator

---

## Question 4 - `grade_analyzer(grades)`

**User Story:**
*As a university professor reviewing end-of-year results, I need to determine if a student passes overall based on their course grades, where they must pass ALL courses (60% or above in each) to proceed to the next year.*

**Requirements:**
- Accept a list of grade percentages (integers)
- Return "Pass" if ALL grades are 60 or above
- Return "No Pass" if ANY grade is below 60
- Return "No Pass" for an empty list

**Example:**
```python
grade_analyzer([70, 80, 90, 75])     # Returns: "Pass"
grade_analyzer([80, 50, 90, 40])     # Returns: "No Pass"
grade_analyzer([60, 60, 60])         # Returns: "Pass"
grade_analyzer([])                   # Returns: "No Pass"
```

**Implementation Notes:**
- Loop through all grades
- Check if any grade is below 60
- Can use `all()` function with list comprehension
- Empty list should return "No Pass"

---

## Question 5 - `valley_finder(data)`

**User Story:**
*As a stock market analyst studying price fluctuations, I need to identify valley points (prices lower than both surrounding days) to detect potential buying opportunities in historical trading data.*

**Requirements:**
- Accept a list of numerical values
- Return a list of all valley values (values lower than both neighbors)
- A valley must be strictly lower than both neighbors (not equal)
- Edge values (first and last) cannot be valleys
- Return empty list if no valleys found

**Example:**
```python
valley_finder([10, 3, 8, 2, 9, 1, 7])  # Returns: [3, 2, 1]
valley_finder([5, 4, 3, 2, 1])         # Returns: []
valley_finder([5, 2, 7])               # Returns: [2]
valley_finder([5, 2, 2, 5])            # Returns: [] (2 == 2, not strictly lower)
```

**Implementation Notes:**
- Loop from index 1 to len(data) - 1 (exclude edges)
- Check if `data[i] < data[i-1]` AND `data[i] < data[i+1]`
- Plateaus (equal values) are NOT valleys

---

## Question 6 - `email_validator(email_list)`

**User Story:**
*As a marketing manager preparing an email campaign, I need to validate all email addresses in my contact list to separate valid addresses from invalid ones, so I can clean my database and avoid bounce-backs.*

**Requirements:**
- Accept a list of email strings
- Return a dictionary with two keys: 'valid_emails' and 'invalid_emails'
- Valid email must contain:
  - Exactly one '@' symbol
  - At least one character before '@'
  - At least one '.' after '@'
  - At least one character after the last '.'
- Return empty lists for empty input

**Example:**
```python
email_validator(['test@example.com', 'invalid.email'])
# Returns: {
#     'valid_emails': ['test@example.com'],
#     'invalid_emails': ['invalid.email']
# }

email_validator([])
# Returns: {'valid_emails': [], 'invalid_emails': []}
```

**Implementation Notes:**
- Check for single '@' symbol using `count('@')`
- Split on '@' to check parts
- Check for '.' in domain part
- Use regular expressions (optional) or string methods

---

## Question 7 - `budget_tracker(budget, daily_expenses)`

**User Story:**
*As a backpacker traveling through Europe on a tight budget, I need to track my daily spending to know if I'm staying within budget or if I'm overspending, so I can adjust my plans before running out of money.*

**Requirements:**
- Accept initial budget (integer) and daily expenses (list of integers)
- Simulate spending day by day
- Return different messages based on outcome:
  - If budget exceeded during any day: `"Budget exceeded on day X!"` (X = 1-indexed day)
  - If budget exactly matches total expenses: `"Budget balanced perfectly!"`
  - If budget has surplus after all days: `"Budget surplus: R X"` (X = remaining amount)

**Example:**
```python
budget_tracker(500, [100, 150, 200])
# Day 1: 500 - 100 = 400
# Day 2: 400 - 150 = 250
# Day 3: 250 - 200 = 50
# Returns: "Budget surplus: R 50"

budget_tracker(200, [50, 75, 100, 50])
# Day 1: 200 - 50 = 150
# Day 2: 150 - 75 = 75
# Day 3: 75 - 100 = -25 (exceeded!)
# Returns: "Budget exceeded on day 3!"

budget_tracker(300, [100, 100, 100])
# Returns: "Budget balanced perfectly!"
```

**Implementation Notes:**
- Loop through expenses, tracking current budget
- Check after each day if budget goes negative
- Use enumerate() to track day number (add 1 for 1-indexed)
- Check final budget: negative (exceeded), zero (balanced), positive (surplus)

---

# Your Goal

Complete all functions in `loopy_new.py` so that:
- The code is valid Python
- Each function behaves according to the requirements above
- All unit tests pass successfully

## Tips for Success

1. **Read the user story and requirements carefully** - understand the real-world context
2. **Test incrementally** - run tests for one function at a time
3. **Pay attention to edge cases** - empty lists, zero values, boundary conditions
4. **Use appropriate loop types** - for loops, while loops, list comprehensions
5. **Follow exact output format** - especially for string returns and print statements
6. **Handle both positive and negative numbers** where applicable

## Common Pitfalls to Avoid

- ❌ Off-by-one errors in loops (especially with indices)
- ❌ Forgetting to handle empty lists
- ❌ Not checking edge cases (first/last elements)
- ❌ Incorrect string formatting (spaces, capitalization, punctuation)
- ❌ Using equality when strict comparison is needed (valleys)
- ❌ Forgetting to convert types (int, float, str)

## Function Summary Table

| Function | Input | Output | Key Concept |
|----------|-------|--------|-------------|
| `recipe_scaler` | list, multiplier | list | List transformation |
| `temperature_converter` | list of Celsius | list of Fahrenheit | Mathematical conversion |
| `password_strength` | (uses input()) | prints messages | Input validation loop |
| `grade_analyzer` | list of grades | "Pass"/"No Pass" | Conditional aggregation |
| `valley_finder` | list of values | list of valleys | Neighbor comparison |
| `email_validator` | list of emails | dict with valid/invalid | String validation |
| `budget_tracker` | budget, expenses | status message | Day-by-day simulation |

Good luck! 🚀