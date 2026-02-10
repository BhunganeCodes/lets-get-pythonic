# data-structures-400 - Python Data Structures & Algorithms

# Learning Outcomes assessed:

- List manipulation and transformation
- Dictionary operations and grouping
- Tuple unpacking and processing
- Set operations
- Nested data structures
- Algorithm design
- Recursion
- Error handling
- Edge case management

---

# Assessment Structure

This is a coding-only assessment with 7 Python programming challenges focused on data structures and algorithms.

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
python3 -m pytest test_data_structures_new.py -v
```

To run your tests individually:

```bash
python3 -m pytest test_data_structures_new.py::test_matrix_transposer_logic -v
```

---

# Data Structures Coding Assessment

This assessment consists of seven Python functions that test your mastery of data structures, algorithms, and problem-solving.

## Project Structure

```
data-structures-assessment/
├── data_structures_new.py          # <-- This is where you write your solutions
├── test_data_structures_new.py     # <-- These are the tests you must make pass
└── README.md                        # <-- Assessment instructions (this file) 
```

---

## Question 1 - `matrix_transposer(matrix)`

**User Story:**
*As a data scientist working with sensor arrays, I need to transpose measurement matrices (swap rows and columns) to align time-series data from multiple sensors for analysis in my machine learning pipeline.*

**Requirements:**
- Accept a 2D list (matrix) as input
- Return the transposed matrix (rows become columns, columns become rows)
- Return empty list for empty input
- All rows must have the same length (rectangular matrix)
- Raise `ValueError` if rows have different lengths
- Raise `TypeError` if any row is not a list

**Example:**
```python
matrix_transposer([[1, 2, 3], [4, 5, 6]])
# Returns: [[1, 4], [2, 5], [3, 6]]

matrix_transposer([[1, 2], [3, 4], [5, 6]])
# Returns: [[1, 3, 5], [2, 4, 6]]

matrix_transposer([[1]])
# Returns: [[1]]

matrix_transposer([])
# Returns: []
```

**Implementation Notes:**
- Can use nested loops or list comprehension with zip()
- Check that all rows have equal length
- Handle edge cases: empty matrix, single element, single row, single column

---

## Question 2 - `priority_queue_mapper(tasks)`

**User Story:**
*As a task management application developer, I need to organize incoming tasks by their priority levels, grouping all tasks with the same priority together so users can focus on high-priority items first.*

**Requirements:**
- Accept a list of tuples: `(task_name, priority_level)`
- Return a dictionary where keys are priority levels and values are lists of task names
- Tasks with the same priority should be grouped together
- Return empty dict for empty input
- Raise `ValueError` if tuple doesn't have exactly 2 elements
- Raise `TypeError` if priority is not an integer

**Example:**
```python
priority_queue_mapper([("task1", 1), ("task2", 2), ("task3", 1)])
# Returns: {1: ["task1", "task3"], 2: ["task2"]}

priority_queue_mapper([("urgent", 3)])
# Returns: {3: ["urgent"]}

priority_queue_mapper([])
# Returns: {}
```

**Implementation Notes:**
- Use dictionary with setdefault() or defaultdict
- Loop through tasks and group by priority
- Preserve order of tasks within each priority

---

## Question 3 - `merge_sorted_lists(list1, list2)`

**User Story:**
*As a streaming service engineer merging two sorted playlists (one from user favorites, one from recommendations), I need to combine them into a single sorted playlist without re-sorting the entire dataset for optimal performance.*

**Requirements:**
- Accept two sorted lists (ascending order)
- Return a single merged sorted list
- Must maintain sorted order
- Handle empty lists
- Raise `ValueError` if either input list is not sorted
- Should work with negative numbers and duplicates

**Example:**
```python
merge_sorted_lists([1, 3, 5], [2, 4, 6])
# Returns: [1, 2, 3, 4, 5, 6]

merge_sorted_lists([], [1, 2, 3])
# Returns: [1, 2, 3]

merge_sorted_lists([1, 2, 3], [4, 5, 6])
# Returns: [1, 2, 3, 4, 5, 6]
```

**Implementation Notes:**
- Use two-pointer technique for efficiency
- Compare elements from both lists
- Don't just concatenate and sort (defeats the purpose)
- Check if inputs are sorted before processing

---

## Question 4 - `inventory_grouper(products)`

**User Story:**
*As a warehouse analytics manager, I need to aggregate product inventory by category, calculating total stock per category and tracking all SKUs in each category for supply chain optimization reports.*

**Requirements:**
- Accept a list of product dictionaries with keys: `sku`, `category`, `stock`
- Return a dictionary where:
  - Keys are category names
  - Values are dicts with `total_stock` (sum) and `skus` (list of SKU codes)
- Return empty dict for empty input
- Raise `KeyError` if required keys are missing
- Raise `TypeError` if element is not a dict

**Example:**
```python
inventory_grouper([
    {"sku": "A001", "category": "Electronics", "stock": 50}, 
    {"sku": "A003", "category": "Electronics", "stock": 20},
    {"sku": "B002", "category": "Clothing", "stock": 30}
])
# Returns: {
#     "Electronics": {"total_stock": 70, "skus": ["A001", "A003"]}, 
#     "Clothing": {"total_stock": 30, "skus": ["B002"]}
# }
```

**Implementation Notes:**
- Use nested dictionaries
- Accumulate stock totals per category
- Collect SKUs in lists
- Use setdefault() or defaultdict for cleaner code

---

## Question 5 - `paginator(items, page_size)`

**User Story:**
*As a web developer building an e-commerce product listing page, I need to split large product catalogs into pages of fixed size so users can navigate results efficiently without overwhelming their browser.*

**Requirements:**
- Accept a list of items and a page size (integer)
- Return a list of pages, where each page is a list of items
- Last page may have fewer items than page_size
- Return empty list for empty input
- Raise `ValueError` if page_size is less than 1

**Example:**
```python
paginator(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 3)
# Returns: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]

paginator([1, 2, 3, 4, 5, 6], 2)
# Returns: [[1, 2], [3, 4], [5, 6]]

paginator([], 5)
# Returns: []
```

**Implementation Notes:**
- Use list slicing with step
- Loop in increments of page_size
- Handle partial last page
- Don't modify original list

---

## Question 6 - `graph_degree_counter(graph)`

**User Story:**
*As a social network analyst studying user connectivity patterns, I need to count how many connections (out-degree) each user has in the network to identify influencers and understand network topology.*

**Requirements:**
- Accept a dictionary representing a directed graph (adjacency list)
  - Keys are node names
  - Values are lists of connected nodes
- Return a dictionary with node names as keys and their out-degree (number of outgoing edges) as values
- Return empty dict for empty input
- Raise `TypeError` if value is not iterable

**Example:**
```python
graph_degree_counter({"A": ["B", "C"], "B": ["A"], "C": ["A"]})
# Returns: {"A": 2, "B": 1, "C": 1}

graph_degree_counter({"X": ["Y", "Z"], "Y": ["X", "Z"], "Z": ["X", "Y"]})
# Returns: {"X": 2, "Y": 2, "Z": 2}

graph_degree_counter({})
# Returns: {}
```

**Implementation Notes:**
- Simply count the length of each adjacency list
- Use dictionary comprehension
- Self-loops count as 1 edge
- Empty adjacency lists have degree 0

---

## Question 7 - `factorial_calculator(n)` **[MUST USE RECURSION]**

**User Story:**
*As a mathematics education software developer creating an interactive learning tool, I need to calculate factorials recursively to help students understand the recursive nature of factorial definitions: n! = n × (n-1)!*

**Requirements:**
- Accept a non-negative integer n
- Return n! (n factorial)
- **MUST use recursion** (function calls itself)
- Base case: 0! = 1, 1! = 1
- Recursive case: n! = n × (n-1)!
- Raise `ValueError` for negative numbers or non-integers

**Example:**
```python
factorial_calculator(5)
# Returns: 120 (5 × 4 × 3 × 2 × 1)

factorial_calculator(0)
# Returns: 1

factorial_calculator(10)
# Returns: 3628800
```

**Factorial Reference:**
```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

**Implementation Notes:**
- Base case: if n == 0 or n == 1, return 1
- Recursive case: return n * factorial_calculator(n - 1)
- Validate input before recursion
- **Tests will verify recursion is used** (iterative solutions will fail)

---

# Your Goal

Complete all functions in `data_structures_new.py` so that:
- The code is valid Python
- Each function behaves according to the requirements above
- All unit tests pass successfully
- Question 7 **MUST** use recursion

## Tips for Success

1. **Read the user story and requirements carefully** - understand the real-world application
2. **Test incrementally** - run tests for one function at a time
3. **Pay attention to edge cases** - empty inputs, single elements, boundary conditions
4. **Use appropriate data structures** - lists, dicts, tuples, sets where needed
5. **Handle errors properly** - raise specified exceptions for invalid inputs
6. **For Question 7** - ensure you use recursion, not loops

## Common Pitfalls to Avoid

- ❌ Not validating input data (missing keys, wrong types)
- ❌ Mutating original data structures
- ❌ Forgetting to handle empty inputs
- ❌ Not checking for rectangular matrices (Question 1)
- ❌ Using built-in sort for merge (defeats the purpose - Question 3)
- ❌ Using loops instead of recursion (Question 7)
- ❌ Off-by-one errors in slicing/pagination

## Function Summary Table

| Question | Function | Input | Output | Key Concept |
|----------|----------|-------|--------|-------------|
| 1 | `matrix_transposer` | 2D list | 2D list | Nested loops, zip() |
| 2 | `priority_queue_mapper` | list of tuples | dict | Grouping, dictionaries |
| 3 | `merge_sorted_lists` | 2 sorted lists | merged list | Two-pointer algorithm |
| 4 | `inventory_grouper` | list of dicts | nested dict | Aggregation, grouping |
| 5 | `paginator` | list, page size | list of lists | List slicing |
| 6 | `graph_degree_counter` | adjacency dict | degree dict | Graph theory |
| 7 | `factorial_calculator` | integer | integer | **Recursion** |

## Complexity Expectations

- Most functions should aim for O(n) time complexity
- Question 3 (merge) should NOT use O(n log n) sort
- Question 7 (factorial) will have O(n) time, O(n) space due to recursion

Good luck! 🚀